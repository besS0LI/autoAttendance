import time
from datetime import datetime, timedelta

import schedule

from logger_config import log_message


class SchedulerManager:

    SCHEDULE_CHECK_TIME = "08:50"
    RETRY_INTERVAL = 300  # 5 минут
    ATTENDANCE_WINDOW = timedelta(hours=1, minutes=35)

    def __init__(self, schedule_service, attendance_service):
        self.schedule_service = schedule_service
        self.attendance_service = attendance_service
        self.schedule_loaded_for_date = None

    def _schedule_today(self):
        today = datetime.now().date()

        log_message(f"Получение расписания на {today:%d.%m.%Y}")

        try:
            schedule_data = self.schedule_service.get_schedule()
        except Exception as exc:
            log_message(
                f"Ошибка получения расписания: {type(exc).__name__}: {exc}"
            )
            return False

        schedule.clear()

        if not schedule_data:
            log_message("Сегодня занятий нет")
            self.schedule_loaded_for_date = today
            return True

        now = datetime.now()
        jobs_added = 0
        immediate_lessons = 0

        for lesson_time, lesson_data in schedule_data.items():
            try:
                lesson_start = datetime.strptime(
                    lesson_time, "%H:%M"
                ).replace(
                    year=now.year,
                    month=now.month,
                    day=now.day,
                )
            except ValueError:
                log_message(
                    f"Некорректное время занятия: {lesson_time}"
                )
                continue

            lesson_end = lesson_start + self.ATTENDANCE_WINDOW

            if now < lesson_start:
                schedule.every().day.at(lesson_time).do(
                    self.attendance_service.mark_attendance,
                    lesson_data,
                )
                jobs_added += 1
                continue

            if now <= lesson_end:
                log_message(
                    f"Пара уже началась: {lesson_time} — "
                    f"{lesson_data['name']}. Выполняется отметка."
                )
                self.attendance_service.mark_attendance(lesson_data)
                immediate_lessons += 1

        log_message(
            f"Расписание успешно загружено. "
            f"Будущих задач: {jobs_added}, "
            f"текущих пар: {immediate_lessons}"
        )

        self.schedule_loaded_for_date = today
        return True

    def run(self):
        log_message("Запущен постоянный планировщик")

        while True:
            today = datetime.now().date()

            if (
                self.schedule_loaded_for_date is not None
                and self.schedule_loaded_for_date != today
            ):
                self.schedule_loaded_for_date = None
                schedule.clear()
                log_message(f"Начался новый день: {today:%d.%m.%Y}")

            if self.schedule_loaded_for_date != today:
                now = datetime.now()
                check_time = now.replace(
                    hour=8,
                    minute=50,
                    second=0,
                    microsecond=0,
                )

                if now >= check_time:
                    if not self._schedule_today():
                        time.sleep(self.RETRY_INTERVAL)
                    continue

                seconds = int((check_time - now).total_seconds())
                time.sleep(min(seconds, self.RETRY_INTERVAL))
                continue

            try:
                schedule.run_pending()
            except Exception as exc:
                log_message(
                    f"Ошибка выполнения задачи: {type(exc).__name__}: {exc}"
                )

            time.sleep(5)
