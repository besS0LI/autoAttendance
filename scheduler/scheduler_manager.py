import time
from datetime import datetime, timedelta

import schedule

from logger_config import log_message


class SchedulerManager:

    SCHEDULE_CHECK_TIME = "08:50"
    RETRY_INTERVAL = 300  # 5 минут

    def __init__(self, schedule_service, attendance_service):
        self.schedule_service = schedule_service
        self.attendance_service = attendance_service

        # Дата, за которую расписание уже успешно получено
        self.schedule_loaded_for_date = None

    def _schedule_today(self):
        """
        Получает расписание на сегодня и создаёт задачи на будущие пары.
        Возвращает True, если расписание успешно обработано.
        """

        today = datetime.now().date()

        log_message(
            f"Получение расписания на {today:%d.%m.%Y}"
        )

        try:
            schedule_data = self.schedule_service.get_schedule()
        except Exception as exc:
            log_message(
                f"Ошибка получения расписания: "
                f"{type(exc).__name__}: {exc}"
            )
            return False

        # Сначала удаляем старые задачи на занятия.
        schedule.clear()

        if not schedule_data:
            log_message("Сегодня занятий нет")

            # Расписание успешно получено, просто занятий нет.
            self.schedule_loaded_for_date = today
            return True

        current_time = datetime.now().strftime("%H:%M")

        jobs_added = 0

        for lesson_time, lesson_data in schedule_data.items():

            if lesson_time < current_time:
                log_message(
                    f"Пропущено время занятия {lesson_time} — "
                    f"{lesson_data['name']}"
                )
                continue

            schedule.every().day.at(lesson_time).do(
                self.attendance_service.mark_attendance,
                lesson_data
            )

            log_message(
                f"Добавлена задача {lesson_time} — "
                f"{lesson_data['name']}"
            )

            jobs_added += 1

        log_message(
            f"Расписание успешно загружено. "
            f"Задач на сегодня: {jobs_added}"
        )

        # ВАЖНО: дата устанавливается только после успешной загрузки.
        self.schedule_loaded_for_date = today

        return True

    @staticmethod
    def _seconds_until(time_string):
        """
        Количество секунд до указанного времени сегодня.
        Если время уже прошло — возвращает 0.
        """

        now = datetime.now()

        hour, minute = map(int, time_string.split(":"))

        target = now.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0,
        )

        return max(0, int((target - now).total_seconds()))

    @staticmethod
    def _seconds_until_next_day():
        now = datetime.now()

        tomorrow = (now + timedelta(days=1)).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

        return max(
            1,
            int((tomorrow - now).total_seconds())
        )

    def run(self):
        log_message("Запущен постоянный планировщик")

        while True:

            today = datetime.now().date()

            # Новый день — сбрасываем состояние.
            if (
                self.schedule_loaded_for_date is not None
                and self.schedule_loaded_for_date != today
            ):
                self.schedule_loaded_for_date = None
                schedule.clear()

                log_message(
                    f"Начался новый день: {today:%d.%m.%Y}"
                )

            # Расписание на сегодня ещё не загружено.
            if self.schedule_loaded_for_date != today:

                now = datetime.now()
                check_time = now.replace(
                    hour=8,
                    minute=50,
                    second=0,
                    microsecond=0,
                )

                # Если сейчас уже 08:50 или позже —
                # получаем расписание сразу.
                if now >= check_time:

                    log_message(
                        "Время проверки расписания наступило. "
                        "Загружаем расписание."
                    )

                    success = self._schedule_today()

                    if not success:
                        log_message(
                            "Повторная попытка получения "
                            "расписания через 5 минут"
                        )
                        time.sleep(self.RETRY_INTERVAL)

                    continue

                # Сейчас ещё до 08:50.
                seconds = int(
                    (check_time - now).total_seconds()
                )

                log_message(
                    f"Ожидание 08:50. "
                    f"До проверки: {seconds} секунд"
                )

                # Не спим больше 5 минут, чтобы корректно
                # реагировать на смену дня и перезапуск.
                time.sleep(min(seconds, 300))
                continue

            # Расписание уже успешно загружено.
            try:
                schedule.run_pending()
            except Exception as exc:
                log_message(
                    f"Ошибка выполнения задачи: "
                    f"{type(exc).__name__}: {exc}"
                )

            time.sleep(5)
