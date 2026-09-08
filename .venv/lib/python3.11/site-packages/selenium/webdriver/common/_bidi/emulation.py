# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# This file is generated from the WebDriver BiDi specification.
# DO NOT EDIT. Regenerate with:
#   bazel run //py:generate-bidi-protocol


from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, TypeAlias

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import UNSET, Record, Union, UnsetType, meta, register


@register("emulation.ForcedColorsModeTheme")
class ForcedColorsModeTheme(str, Enum):
    """emulation.ForcedColorsModeTheme.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationforcedcolorsmodetheme
    """

    LIGHT = "light"
    DARK = "dark"


@register("emulation.ScreenOrientationNatural")
class ScreenOrientationNatural(str, Enum):
    """emulation.ScreenOrientationNatural.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationscreenorientationnatural
    """

    PORTRAIT = "portrait"
    LANDSCAPE = "landscape"


@register("emulation.ScreenOrientationType")
class ScreenOrientationType(str, Enum):
    """emulation.ScreenOrientationType.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationscreenorientationtype
    """

    PORTRAIT_PRIMARY = "portrait-primary"
    PORTRAIT_SECONDARY = "portrait-secondary"
    LANDSCAPE_PRIMARY = "landscape-primary"
    LANDSCAPE_SECONDARY = "landscape-secondary"


@register("emulation.SetScrollbarTypeOverrideParametersScrollbarType")
class SetScrollbarTypeOverrideParametersScrollbarType(str, Enum):
    CLASSIC = "classic"
    OVERLAY = "overlay"


@register("emulation.SetForcedColorsModeThemeOverrideParameters")
@dataclass(frozen=True)
class SetForcedColorsModeThemeOverrideParameters(Record):
    """emulation.SetForcedColorsModeThemeOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetforcedcolorsmodethemeoverrideparameters
    """

    theme: ForcedColorsModeTheme | None = field(
        metadata=meta("theme", required=True, nullable=True, enum="emulation.ForcedColorsModeTheme"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.GeolocationCoordinates")
@dataclass(frozen=True)
class GeolocationCoordinates(Record):
    """emulation.GeolocationCoordinates.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationgeolocationcoordinates
    """

    latitude: float = field(metadata=meta("latitude", required=True, primitive="float"))
    longitude: float = field(metadata=meta("longitude", required=True, primitive="float"))
    accuracy: float | UnsetType = field(default=UNSET, metadata=meta("accuracy", primitive="float"))
    altitude: float | None | UnsetType = field(
        default=UNSET,
        metadata=meta("altitude", nullable=True, primitive="float"),
    )
    altitude_accuracy: float | None | UnsetType = field(
        default=UNSET,
        metadata=meta("altitudeAccuracy", nullable=True, primitive="float"),
    )
    heading: float | None | UnsetType = field(
        default=UNSET,
        metadata=meta("heading", nullable=True, primitive="float"),
    )
    speed: float | None | UnsetType = field(default=UNSET, metadata=meta("speed", nullable=True, primitive="float"))


@register("emulation.GeolocationPositionError")
@dataclass(frozen=True)
class GeolocationPositionError(Record):
    """emulation.GeolocationPositionError.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationgeolocationpositionerror
    """

    type: str = field(
        default="positionUnavailable",
        init=False,
        metadata=meta("type", required=True, fixed="positionUnavailable"),
    )


@register("emulation.SetLocaleOverrideParameters")
@dataclass(frozen=True)
class SetLocaleOverrideParameters(Record):
    """emulation.SetLocaleOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetlocaleoverrideparameters
    """

    locale: str | None = field(metadata=meta("locale", required=True, nullable=True, primitive="str"))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetMediaFeaturesOverrideParameters")
@dataclass(frozen=True)
class SetMediaFeaturesOverrideParameters(Record):
    """emulation.SetMediaFeaturesOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetmediafeaturesoverrideparameters
    """

    features: list[MediaFeature] | None = field(
        metadata=meta("features", required=True, nullable=True, ref="emulation.MediaFeature", is_list=True),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.MediaFeature")
@dataclass(frozen=True)
class MediaFeature(Record):
    """emulation.MediaFeature.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationmediafeature
    """

    name: str = field(metadata=meta("name", required=True, primitive="str"))
    value: str = field(metadata=meta("value", required=True, primitive="str"))


@register("emulation.SetNetworkConditionsParameters")
@dataclass(frozen=True)
class SetNetworkConditionsParameters(Record):
    """emulation.SetNetworkConditionsParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetnetworkconditionsparameters
    """

    network_conditions: NetworkConditionsOffline | None = field(
        metadata=meta("networkConditions", required=True, nullable=True, ref="emulation.NetworkConditionsOffline"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.NetworkConditionsOffline")
@dataclass(frozen=True)
class NetworkConditionsOffline(Record):
    """emulation.NetworkConditionsOffline.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationnetworkconditionsoffline
    """

    type: str = field(default="offline", init=False, metadata=meta("type", required=True, fixed="offline"))


@register("emulation.ScreenArea")
@dataclass(frozen=True)
class ScreenArea(Record):
    """emulation.ScreenArea.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationscreenarea
    """

    width: int = field(metadata=meta("width", required=True, primitive="int"))
    height: int = field(metadata=meta("height", required=True, primitive="int"))


@register("emulation.SetScreenSettingsOverrideParameters")
@dataclass(frozen=True)
class SetScreenSettingsOverrideParameters(Record):
    """emulation.SetScreenSettingsOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetscreensettingsoverrideparameters
    """

    screen_area: ScreenArea | None = field(
        metadata=meta("screenArea", required=True, nullable=True, ref="emulation.ScreenArea"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.ScreenOrientation")
@dataclass(frozen=True)
class ScreenOrientation(Record):
    """emulation.ScreenOrientation.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationscreenorientation
    """

    natural: ScreenOrientationNatural = field(
        metadata=meta("natural", required=True, enum="emulation.ScreenOrientationNatural"),
    )
    type: ScreenOrientationType = field(
        metadata=meta("type", required=True, enum="emulation.ScreenOrientationType"),
    )


@register("emulation.SetScreenOrientationOverrideParameters")
@dataclass(frozen=True)
class SetScreenOrientationOverrideParameters(Record):
    """emulation.SetScreenOrientationOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetscreenorientationoverrideparameters
    """

    screen_orientation: ScreenOrientation | None = field(
        metadata=meta("screenOrientation", required=True, nullable=True, ref="emulation.ScreenOrientation"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetUserAgentOverrideParameters")
@dataclass(frozen=True)
class SetUserAgentOverrideParameters(Record):
    """emulation.SetUserAgentOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetuseragentoverrideparameters
    """

    user_agent: str | None = field(metadata=meta("userAgent", required=True, nullable=True, primitive="str"))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetViewportMetaOverrideParameters")
@dataclass(frozen=True)
class SetViewportMetaOverrideParameters(Record):
    """emulation.SetViewportMetaOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetviewportmetaoverrideparameters
    """

    viewport_meta: bool | None = field(metadata=meta("viewportMeta", required=True, nullable=True, fixed=True))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetScriptingEnabledParameters")
@dataclass(frozen=True)
class SetScriptingEnabledParameters(Record):
    """emulation.SetScriptingEnabledParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetscriptingenabledparameters
    """

    enabled: bool | None = field(metadata=meta("enabled", required=True, nullable=True, fixed=False))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetScrollbarTypeOverrideParameters")
@dataclass(frozen=True)
class SetScrollbarTypeOverrideParameters(Record):
    """emulation.SetScrollbarTypeOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetscrollbartypeoverrideparameters
    """

    scrollbar_type: SetScrollbarTypeOverrideParametersScrollbarType | None = field(
        metadata=meta("scrollbarType", required=True, nullable=True, enum="emulation.SetScrollbarTypeOverrideParametersScrollbarType"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetTimezoneOverrideParameters")
@dataclass(frozen=True)
class SetTimezoneOverrideParameters(Record):
    """emulation.SetTimezoneOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsettimezoneoverrideparameters
    """

    timezone: str | None = field(metadata=meta("timezone", required=True, nullable=True, primitive="str"))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetTouchOverrideParameters")
@dataclass(frozen=True)
class SetTouchOverrideParameters(Record):
    """emulation.SetTouchOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsettouchoverrideparameters
    """

    max_touch_points: int | None = field(
        metadata=meta("maxTouchPoints", required=True, nullable=True, primitive="int"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetGeolocationOverrideParameters_Coordinates")
@dataclass(frozen=True)
class SetGeolocationOverrideParametersCoordinates(Record):
    coordinates: GeolocationCoordinates | None = field(
        metadata=meta("coordinates", required=True, nullable=True, ref="emulation.GeolocationCoordinates"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetGeolocationOverrideParameters_Error")
@dataclass(frozen=True)
class SetGeolocationOverrideParametersError(Record):
    error: GeolocationPositionError = field(
        metadata=meta("error", required=True, ref="emulation.GeolocationPositionError"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetGeolocationOverrideParameters")
class SetGeolocationOverrideParameters(Union):
    """emulation.SetGeolocationOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetgeolocationoverrideparameters
    """

    _PRESENCE = (
        ("emulation.SetGeolocationOverrideParameters_Coordinates", ("coordinates",)),
        ("emulation.SetGeolocationOverrideParameters_Error", ("error",)),
    )
    _OBJECT_ONLY = True


SetGeolocationOverrideParametersValue: TypeAlias = (
    "SetGeolocationOverrideParametersCoordinates | SetGeolocationOverrideParametersError"
)


class Emulation(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-emulation
    """

    def set_forced_colors_mode_theme_override(
        self,
        theme: ForcedColorsModeTheme | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setForcedColorsModeThemeOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setForcedColorsModeThemeOverride
        """
        params = SetForcedColorsModeThemeOverrideParameters(
            theme=theme,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setForcedColorsModeThemeOverride", params=params, result=None)

    def set_geolocation_override(
        self,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
        coordinates: GeolocationCoordinates | None | UnsetType = UNSET,
        error: GeolocationPositionError | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setGeolocationOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setGeolocationOverride
        """
        params = SetGeolocationOverrideParameters.build(
            contexts=contexts,
            user_contexts=user_contexts,
            coordinates=coordinates,
            error=error,
        )
        return self._execute("emulation.setGeolocationOverride", params=params, result=None)

    def set_locale_override(
        self,
        locale: str | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setLocaleOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setLocaleOverride
        """
        params = SetLocaleOverrideParameters(locale=locale, contexts=contexts, user_contexts=user_contexts)
        return self._execute("emulation.setLocaleOverride", params=params, result=None)

    def set_media_features_override(
        self,
        features: list[MediaFeature] | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setMediaFeaturesOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setMediaFeaturesOverride
        """
        params = SetMediaFeaturesOverrideParameters(
            features=features,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setMediaFeaturesOverride", params=params, result=None)

    def set_network_conditions(
        self,
        network_conditions: NetworkConditionsOffline | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setNetworkConditions (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setNetworkConditions
        """
        params = SetNetworkConditionsParameters(
            network_conditions=network_conditions,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setNetworkConditions", params=params, result=None)

    def set_screen_orientation_override(
        self,
        screen_orientation: ScreenOrientation | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setScreenOrientationOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setScreenOrientationOverride
        """
        params = SetScreenOrientationOverrideParameters(
            screen_orientation=screen_orientation,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setScreenOrientationOverride", params=params, result=None)

    def set_screen_settings_override(
        self,
        screen_area: ScreenArea | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setScreenSettingsOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setScreenSettingsOverride
        """
        params = SetScreenSettingsOverrideParameters(
            screen_area=screen_area,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setScreenSettingsOverride", params=params, result=None)

    def set_scripting_enabled(
        self,
        enabled: bool | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setScriptingEnabled (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setScriptingEnabled
        """
        params = SetScriptingEnabledParameters(enabled=enabled, contexts=contexts, user_contexts=user_contexts)
        return self._execute("emulation.setScriptingEnabled", params=params, result=None)

    def set_scrollbar_type_override(
        self,
        scrollbar_type: SetScrollbarTypeOverrideParametersScrollbarType | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setScrollbarTypeOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setScrollbarTypeOverride
        """
        params = SetScrollbarTypeOverrideParameters(
            scrollbar_type=scrollbar_type,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setScrollbarTypeOverride", params=params, result=None)

    def set_timezone_override(
        self,
        timezone: str | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setTimezoneOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setTimezoneOverride
        """
        params = SetTimezoneOverrideParameters(
            timezone=timezone,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setTimezoneOverride", params=params, result=None)

    def set_touch_override(
        self,
        max_touch_points: int | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setTouchOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setTouchOverride
        """
        params = SetTouchOverrideParameters(
            max_touch_points=max_touch_points,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setTouchOverride", params=params, result=None)

    def set_user_agent_override(
        self,
        user_agent: str | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setUserAgentOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setUserAgentOverride
        """
        params = SetUserAgentOverrideParameters(
            user_agent=user_agent,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setUserAgentOverride", params=params, result=None)

    def set_viewport_meta_override(
        self,
        viewport_meta: bool | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setViewportMetaOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setViewportMetaOverride
        """
        params = SetViewportMetaOverrideParameters(
            viewport_meta=viewport_meta,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setViewportMetaOverride", params=params, result=None)
