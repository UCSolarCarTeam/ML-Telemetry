from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Motor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LeftMotor: _ClassVar[Motor]
    RightMotor: _ClassVar[Motor]
LeftMotor: Motor
RightMotor: Motor

class CoordUpdateResponse(_message.Message):
    __slots__ = ("coords", "error")
    COORDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    coords: Coords
    error: Error
    def __init__(self, coords: _Optional[_Union[Coords, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class Coords(_message.Message):
    __slots__ = ("lat", "long")
    LAT_FIELD_NUMBER: _ClassVar[int]
    LONG_FIELD_NUMBER: _ClassVar[int]
    lat: float
    long: float
    def __init__(self, lat: _Optional[float] = ..., long: _Optional[float] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("error", "invalidFields")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INVALIDFIELDS_FIELD_NUMBER: _ClassVar[int]
    error: str
    invalidFields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[str] = ..., invalidFields: _Optional[_Iterable[str]] = ...) -> None: ...

class CoordInfoUpdate(_message.Message):
    __slots__ = ("lat", "long", "password")
    LAT_FIELD_NUMBER: _ClassVar[int]
    LONG_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    lat: str
    long: str
    password: str
    def __init__(self, lat: _Optional[str] = ..., long: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ITelemetryData(_message.Message):
    __slots__ = ("AuxBms", "Battery", "BatteryFaults", "Ccs", "DriverControls", "KeyMotor", "Lights", "MPPT", "MotorDetails", "MotorFaults", "PacketTitle", "TimeStamp")
    AUXBMS_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    BATTERYFAULTS_FIELD_NUMBER: _ClassVar[int]
    CCS_FIELD_NUMBER: _ClassVar[int]
    DRIVERCONTROLS_FIELD_NUMBER: _ClassVar[int]
    KEYMOTOR_FIELD_NUMBER: _ClassVar[int]
    LIGHTS_FIELD_NUMBER: _ClassVar[int]
    MPPT_FIELD_NUMBER: _ClassVar[int]
    MOTORDETAILS_FIELD_NUMBER: _ClassVar[int]
    MOTORFAULTS_FIELD_NUMBER: _ClassVar[int]
    PACKETTITLE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AuxBms: IAuxBms
    Battery: IBattery
    BatteryFaults: IBatteryFault
    Ccs: ICcs
    DriverControls: IDriverControls
    KeyMotor: _containers.RepeatedCompositeFieldContainer[IKeyMotor]
    Lights: ILights
    MPPT: _containers.RepeatedCompositeFieldContainer[IMPPT]
    MotorDetails: _containers.RepeatedCompositeFieldContainer[IMotorDetail]
    MotorFaults: _containers.RepeatedCompositeFieldContainer[IMotorFault]
    PacketTitle: str
    TimeStamp: int
    def __init__(self, AuxBms: _Optional[_Union[IAuxBms, _Mapping]] = ..., Battery: _Optional[_Union[IBattery, _Mapping]] = ..., BatteryFaults: _Optional[_Union[IBatteryFault, _Mapping]] = ..., Ccs: _Optional[_Union[ICcs, _Mapping]] = ..., DriverControls: _Optional[_Union[IDriverControls, _Mapping]] = ..., KeyMotor: _Optional[_Iterable[_Union[IKeyMotor, _Mapping]]] = ..., Lights: _Optional[_Union[ILights, _Mapping]] = ..., MPPT: _Optional[_Iterable[_Union[IMPPT, _Mapping]]] = ..., MotorDetails: _Optional[_Iterable[_Union[IMotorDetail, _Mapping]]] = ..., MotorFaults: _Optional[_Iterable[_Union[IMotorFault, _Mapping]]] = ..., PacketTitle: _Optional[str] = ..., TimeStamp: _Optional[int] = ...) -> None: ...

class ILapData(_message.Message):
    __slots__ = ("ampHours", "averagePackCurrent", "averageSpeed", "batterySecondsRemaining", "distance", "lapTime", "netPowerOut", "timeStamp", "totalPowerIn", "totalPowerOut")
    AMPHOURS_FIELD_NUMBER: _ClassVar[int]
    AVERAGEPACKCURRENT_FIELD_NUMBER: _ClassVar[int]
    AVERAGESPEED_FIELD_NUMBER: _ClassVar[int]
    BATTERYSECONDSREMAINING_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    LAPTIME_FIELD_NUMBER: _ClassVar[int]
    NETPOWEROUT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOTALPOWERIN_FIELD_NUMBER: _ClassVar[int]
    TOTALPOWEROUT_FIELD_NUMBER: _ClassVar[int]
    ampHours: float
    averagePackCurrent: float
    averageSpeed: float
    batterySecondsRemaining: float
    distance: float
    lapTime: float
    netPowerOut: float
    timeStamp: int
    totalPowerIn: float
    totalPowerOut: float
    def __init__(self, ampHours: _Optional[float] = ..., averagePackCurrent: _Optional[float] = ..., averageSpeed: _Optional[float] = ..., batterySecondsRemaining: _Optional[float] = ..., distance: _Optional[float] = ..., lapTime: _Optional[float] = ..., netPowerOut: _Optional[float] = ..., timeStamp: _Optional[int] = ..., totalPowerIn: _Optional[float] = ..., totalPowerOut: _Optional[float] = ...) -> None: ...

class IAuxBms(_message.Message):
    __slots__ = ("AllowCharge", "AllowDischarge", "AuxBmsAlive", "AuxVoltage", "ChargeContactorError", "ChargeNotClosedDueToHighCurrent", "ChargeOpenButShouldBeClosed", "ChargeShouldTrip", "ChargeTripDueToHighCellVoltage", "ChargeTripDueToHighTemperatureAndCurrent", "ChargeTripDueToPackCurrent", "CommonContactorError", "DischargeContactorError", "DischargeNotClosedDueToHighCurrent", "DischargeOpenButShouldBeClosed", "DischargeShouldTrip", "DischargeTripDueToHighTemperatureAndCurrent", "DischargeTripDueToLowCellVoltage", "DischargeTripDueToPackCurrent", "HighVoltageEnableState", "OrionCANReceivedRecently", "PrechargeState", "ProtectionTrip", "StrobeBmsLight", "TripDueToOrionMessageTimeout")
    ALLOWCHARGE_FIELD_NUMBER: _ClassVar[int]
    ALLOWDISCHARGE_FIELD_NUMBER: _ClassVar[int]
    AUXBMSALIVE_FIELD_NUMBER: _ClassVar[int]
    AUXVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    CHARGECONTACTORERROR_FIELD_NUMBER: _ClassVar[int]
    CHARGENOTCLOSEDDUETOHIGHCURRENT_FIELD_NUMBER: _ClassVar[int]
    CHARGEOPENBUTSHOULDBECLOSED_FIELD_NUMBER: _ClassVar[int]
    CHARGESHOULDTRIP_FIELD_NUMBER: _ClassVar[int]
    CHARGETRIPDUETOHIGHCELLVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    CHARGETRIPDUETOHIGHTEMPERATUREANDCURRENT_FIELD_NUMBER: _ClassVar[int]
    CHARGETRIPDUETOPACKCURRENT_FIELD_NUMBER: _ClassVar[int]
    COMMONCONTACTORERROR_FIELD_NUMBER: _ClassVar[int]
    DISCHARGECONTACTORERROR_FIELD_NUMBER: _ClassVar[int]
    DISCHARGENOTCLOSEDDUETOHIGHCURRENT_FIELD_NUMBER: _ClassVar[int]
    DISCHARGEOPENBUTSHOULDBECLOSED_FIELD_NUMBER: _ClassVar[int]
    DISCHARGESHOULDTRIP_FIELD_NUMBER: _ClassVar[int]
    DISCHARGETRIPDUETOHIGHTEMPERATUREANDCURRENT_FIELD_NUMBER: _ClassVar[int]
    DISCHARGETRIPDUETOLOWCELLVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    DISCHARGETRIPDUETOPACKCURRENT_FIELD_NUMBER: _ClassVar[int]
    HIGHVOLTAGEENABLESTATE_FIELD_NUMBER: _ClassVar[int]
    ORIONCANRECEIVEDRECENTLY_FIELD_NUMBER: _ClassVar[int]
    PRECHARGESTATE_FIELD_NUMBER: _ClassVar[int]
    PROTECTIONTRIP_FIELD_NUMBER: _ClassVar[int]
    STROBEBMSLIGHT_FIELD_NUMBER: _ClassVar[int]
    TRIPDUETOORIONMESSAGETIMEOUT_FIELD_NUMBER: _ClassVar[int]
    AllowCharge: bool
    AllowDischarge: bool
    AuxBmsAlive: bool
    AuxVoltage: float
    ChargeContactorError: bool
    ChargeNotClosedDueToHighCurrent: bool
    ChargeOpenButShouldBeClosed: bool
    ChargeShouldTrip: bool
    ChargeTripDueToHighCellVoltage: bool
    ChargeTripDueToHighTemperatureAndCurrent: bool
    ChargeTripDueToPackCurrent: bool
    CommonContactorError: bool
    DischargeContactorError: bool
    DischargeNotClosedDueToHighCurrent: bool
    DischargeOpenButShouldBeClosed: bool
    DischargeShouldTrip: bool
    DischargeTripDueToHighTemperatureAndCurrent: bool
    DischargeTripDueToLowCellVoltage: bool
    DischargeTripDueToPackCurrent: bool
    HighVoltageEnableState: bool
    OrionCANReceivedRecently: bool
    PrechargeState: str
    ProtectionTrip: bool
    StrobeBmsLight: bool
    TripDueToOrionMessageTimeout: bool
    def __init__(self, AllowCharge: bool = ..., AllowDischarge: bool = ..., AuxBmsAlive: bool = ..., AuxVoltage: _Optional[float] = ..., ChargeContactorError: bool = ..., ChargeNotClosedDueToHighCurrent: bool = ..., ChargeOpenButShouldBeClosed: bool = ..., ChargeShouldTrip: bool = ..., ChargeTripDueToHighCellVoltage: bool = ..., ChargeTripDueToHighTemperatureAndCurrent: bool = ..., ChargeTripDueToPackCurrent: bool = ..., CommonContactorError: bool = ..., DischargeContactorError: bool = ..., DischargeNotClosedDueToHighCurrent: bool = ..., DischargeOpenButShouldBeClosed: bool = ..., DischargeShouldTrip: bool = ..., DischargeTripDueToHighTemperatureAndCurrent: bool = ..., DischargeTripDueToLowCellVoltage: bool = ..., DischargeTripDueToPackCurrent: bool = ..., HighVoltageEnableState: bool = ..., OrionCANReceivedRecently: bool = ..., PrechargeState: _Optional[str] = ..., ProtectionTrip: bool = ..., StrobeBmsLight: bool = ..., TripDueToOrionMessageTimeout: bool = ...) -> None: ...

class IKeyMotor(_message.Message):
    __slots__ = ("Alive", "BusCurrent", "BusVoltage", "SetCurrent", "SetVelocity", "VehicleVelocity")
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    BUSCURRENT_FIELD_NUMBER: _ClassVar[int]
    BUSVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    SETCURRENT_FIELD_NUMBER: _ClassVar[int]
    SETVELOCITY_FIELD_NUMBER: _ClassVar[int]
    VEHICLEVELOCITY_FIELD_NUMBER: _ClassVar[int]
    Alive: bool
    BusCurrent: float
    BusVoltage: float
    SetCurrent: float
    SetVelocity: float
    VehicleVelocity: float
    def __init__(self, Alive: bool = ..., BusCurrent: _Optional[float] = ..., BusVoltage: _Optional[float] = ..., SetCurrent: _Optional[float] = ..., SetVelocity: _Optional[float] = ..., VehicleVelocity: _Optional[float] = ...) -> None: ...

class IMotorDetail(_message.Message):
    __slots__ = ("BackEmf", "DcBusAmpHours", "DspBoardTemp", "HeatSinkTemp", "MotorCurrentImaginary", "MotorCurrentReal", "MotorTemp", "MotorVoltageImaginary", "MotorVoltageReal", "Odometer", "PhaseBCurrent", "PhaseCCurrent", "SlipSpeed", "VoltageRail15VSupply", "VoltageRail1VSupply", "VoltageRail3VSupply")
    BACKEMF_FIELD_NUMBER: _ClassVar[int]
    DCBUSAMPHOURS_FIELD_NUMBER: _ClassVar[int]
    DSPBOARDTEMP_FIELD_NUMBER: _ClassVar[int]
    HEATSINKTEMP_FIELD_NUMBER: _ClassVar[int]
    MOTORCURRENTIMAGINARY_FIELD_NUMBER: _ClassVar[int]
    MOTORCURRENTREAL_FIELD_NUMBER: _ClassVar[int]
    MOTORTEMP_FIELD_NUMBER: _ClassVar[int]
    MOTORVOLTAGEIMAGINARY_FIELD_NUMBER: _ClassVar[int]
    MOTORVOLTAGEREAL_FIELD_NUMBER: _ClassVar[int]
    ODOMETER_FIELD_NUMBER: _ClassVar[int]
    PHASEBCURRENT_FIELD_NUMBER: _ClassVar[int]
    PHASECCURRENT_FIELD_NUMBER: _ClassVar[int]
    SLIPSPEED_FIELD_NUMBER: _ClassVar[int]
    VOLTAGERAIL15VSUPPLY_FIELD_NUMBER: _ClassVar[int]
    VOLTAGERAIL1VSUPPLY_FIELD_NUMBER: _ClassVar[int]
    VOLTAGERAIL3VSUPPLY_FIELD_NUMBER: _ClassVar[int]
    BackEmf: float
    DcBusAmpHours: float
    DspBoardTemp: float
    HeatSinkTemp: float
    MotorCurrentImaginary: float
    MotorCurrentReal: float
    MotorTemp: float
    MotorVoltageImaginary: float
    MotorVoltageReal: float
    Odometer: float
    PhaseBCurrent: float
    PhaseCCurrent: float
    SlipSpeed: float
    VoltageRail15VSupply: float
    VoltageRail1VSupply: float
    VoltageRail3VSupply: float
    def __init__(self, BackEmf: _Optional[float] = ..., DcBusAmpHours: _Optional[float] = ..., DspBoardTemp: _Optional[float] = ..., HeatSinkTemp: _Optional[float] = ..., MotorCurrentImaginary: _Optional[float] = ..., MotorCurrentReal: _Optional[float] = ..., MotorTemp: _Optional[float] = ..., MotorVoltageImaginary: _Optional[float] = ..., MotorVoltageReal: _Optional[float] = ..., Odometer: _Optional[float] = ..., PhaseBCurrent: _Optional[float] = ..., PhaseCCurrent: _Optional[float] = ..., SlipSpeed: _Optional[float] = ..., VoltageRail15VSupply: _Optional[float] = ..., VoltageRail1VSupply: _Optional[float] = ..., VoltageRail3VSupply: _Optional[float] = ...) -> None: ...

class IDriverControls(_message.Message):
    __slots__ = ("Acceleration", "Alive", "Aux", "Brakes", "Forward", "Hazard", "HeadlightsHigh", "HeadlightsLow", "HeadlightsOff", "Horn", "Interior", "Lap", "NextSong", "PrevSong", "PushToTalk", "RegenBraking", "Reset", "Reverse", "SignalLeft", "SignalRight", "VolumeDown", "VolumeUp")
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    AUX_FIELD_NUMBER: _ClassVar[int]
    BRAKES_FIELD_NUMBER: _ClassVar[int]
    FORWARD_FIELD_NUMBER: _ClassVar[int]
    HAZARD_FIELD_NUMBER: _ClassVar[int]
    HEADLIGHTSHIGH_FIELD_NUMBER: _ClassVar[int]
    HEADLIGHTSLOW_FIELD_NUMBER: _ClassVar[int]
    HEADLIGHTSOFF_FIELD_NUMBER: _ClassVar[int]
    HORN_FIELD_NUMBER: _ClassVar[int]
    INTERIOR_FIELD_NUMBER: _ClassVar[int]
    LAP_FIELD_NUMBER: _ClassVar[int]
    NEXTSONG_FIELD_NUMBER: _ClassVar[int]
    PREVSONG_FIELD_NUMBER: _ClassVar[int]
    PUSHTOTALK_FIELD_NUMBER: _ClassVar[int]
    REGENBRAKING_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    SIGNALLEFT_FIELD_NUMBER: _ClassVar[int]
    SIGNALRIGHT_FIELD_NUMBER: _ClassVar[int]
    VOLUMEDOWN_FIELD_NUMBER: _ClassVar[int]
    VOLUMEUP_FIELD_NUMBER: _ClassVar[int]
    Acceleration: float
    Alive: bool
    Aux: bool
    Brakes: bool
    Forward: bool
    Hazard: bool
    HeadlightsHigh: bool
    HeadlightsLow: bool
    HeadlightsOff: bool
    Horn: bool
    Interior: bool
    Lap: bool
    NextSong: bool
    PrevSong: bool
    PushToTalk: bool
    RegenBraking: float
    Reset: bool
    Reverse: bool
    SignalLeft: bool
    SignalRight: bool
    VolumeDown: bool
    VolumeUp: bool
    def __init__(self, Acceleration: _Optional[float] = ..., Alive: bool = ..., Aux: bool = ..., Brakes: bool = ..., Forward: bool = ..., Hazard: bool = ..., HeadlightsHigh: bool = ..., HeadlightsLow: bool = ..., HeadlightsOff: bool = ..., Horn: bool = ..., Interior: bool = ..., Lap: bool = ..., NextSong: bool = ..., PrevSong: bool = ..., PushToTalk: bool = ..., RegenBraking: _Optional[float] = ..., Reset: bool = ..., Reverse: bool = ..., SignalLeft: bool = ..., SignalRight: bool = ..., VolumeDown: bool = ..., VolumeUp: bool = ...) -> None: ...

class ILights(_message.Message):
    __slots__ = ("Alive", "BmsStrobeLight", "Brakes", "HighBeams", "LeftSignal", "LowBeams", "RightSignal")
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    BMSSTROBELIGHT_FIELD_NUMBER: _ClassVar[int]
    BRAKES_FIELD_NUMBER: _ClassVar[int]
    HIGHBEAMS_FIELD_NUMBER: _ClassVar[int]
    LEFTSIGNAL_FIELD_NUMBER: _ClassVar[int]
    LOWBEAMS_FIELD_NUMBER: _ClassVar[int]
    RIGHTSIGNAL_FIELD_NUMBER: _ClassVar[int]
    Alive: bool
    BmsStrobeLight: bool
    Brakes: bool
    HighBeams: bool
    LeftSignal: bool
    LowBeams: bool
    RightSignal: bool
    def __init__(self, Alive: bool = ..., BmsStrobeLight: bool = ..., Brakes: bool = ..., HighBeams: bool = ..., LeftSignal: bool = ..., LowBeams: bool = ..., RightSignal: bool = ...) -> None: ...

class IBatteryFault(_message.Message):
    __slots__ = ("ErrorFlags", "LimitFlags")
    ERRORFLAGS_FIELD_NUMBER: _ClassVar[int]
    LIMITFLAGS_FIELD_NUMBER: _ClassVar[int]
    ErrorFlags: IBatteryErrorFlags
    LimitFlags: IBatteryLimitFlags
    def __init__(self, ErrorFlags: _Optional[_Union[IBatteryErrorFlags, _Mapping]] = ..., LimitFlags: _Optional[_Union[IBatteryLimitFlags, _Mapping]] = ...) -> None: ...

class IBatteryErrorFlags(_message.Message):
    __slots__ = ("PowerSupplyFault", "AlwaysOnSupplyFault", "CANBUSCommunicationsFault", "ChargeLimitEnforcementFault", "ChargerSafetyRelayFault", "CurrentSensorFault", "DischargeLimitEnforcementFault", "FanMonitorFault", "HighVoltageIsolationFault", "InternalCommunicationFault", "InternalConversionFault", "InternalLogicFault", "InternalMemoryFault", "InternalThermistorsFault", "LowCellVoltageFault", "OpenWiringFault", "PackVoltageSensorFault", "ThermistorFault", "VoltageRedundancyFault", "WeakCellFault", "WeakPackFault")
    POWERSUPPLYFAULT_FIELD_NUMBER: _ClassVar[int]
    ALWAYSONSUPPLYFAULT_FIELD_NUMBER: _ClassVar[int]
    CANBUSCOMMUNICATIONSFAULT_FIELD_NUMBER: _ClassVar[int]
    CHARGELIMITENFORCEMENTFAULT_FIELD_NUMBER: _ClassVar[int]
    CHARGERSAFETYRELAYFAULT_FIELD_NUMBER: _ClassVar[int]
    CURRENTSENSORFAULT_FIELD_NUMBER: _ClassVar[int]
    DISCHARGELIMITENFORCEMENTFAULT_FIELD_NUMBER: _ClassVar[int]
    FANMONITORFAULT_FIELD_NUMBER: _ClassVar[int]
    HIGHVOLTAGEISOLATIONFAULT_FIELD_NUMBER: _ClassVar[int]
    INTERNALCOMMUNICATIONFAULT_FIELD_NUMBER: _ClassVar[int]
    INTERNALCONVERSIONFAULT_FIELD_NUMBER: _ClassVar[int]
    INTERNALLOGICFAULT_FIELD_NUMBER: _ClassVar[int]
    INTERNALMEMORYFAULT_FIELD_NUMBER: _ClassVar[int]
    INTERNALTHERMISTORSFAULT_FIELD_NUMBER: _ClassVar[int]
    LOWCELLVOLTAGEFAULT_FIELD_NUMBER: _ClassVar[int]
    OPENWIRINGFAULT_FIELD_NUMBER: _ClassVar[int]
    PACKVOLTAGESENSORFAULT_FIELD_NUMBER: _ClassVar[int]
    THERMISTORFAULT_FIELD_NUMBER: _ClassVar[int]
    VOLTAGEREDUNDANCYFAULT_FIELD_NUMBER: _ClassVar[int]
    WEAKCELLFAULT_FIELD_NUMBER: _ClassVar[int]
    WEAKPACKFAULT_FIELD_NUMBER: _ClassVar[int]
    PowerSupplyFault: bool
    AlwaysOnSupplyFault: bool
    CANBUSCommunicationsFault: bool
    ChargeLimitEnforcementFault: bool
    ChargerSafetyRelayFault: bool
    CurrentSensorFault: bool
    DischargeLimitEnforcementFault: bool
    FanMonitorFault: bool
    HighVoltageIsolationFault: bool
    InternalCommunicationFault: bool
    InternalConversionFault: bool
    InternalLogicFault: bool
    InternalMemoryFault: bool
    InternalThermistorsFault: bool
    LowCellVoltageFault: bool
    OpenWiringFault: bool
    PackVoltageSensorFault: bool
    ThermistorFault: bool
    VoltageRedundancyFault: bool
    WeakCellFault: bool
    WeakPackFault: bool
    def __init__(self, PowerSupplyFault: bool = ..., AlwaysOnSupplyFault: bool = ..., CANBUSCommunicationsFault: bool = ..., ChargeLimitEnforcementFault: bool = ..., ChargerSafetyRelayFault: bool = ..., CurrentSensorFault: bool = ..., DischargeLimitEnforcementFault: bool = ..., FanMonitorFault: bool = ..., HighVoltageIsolationFault: bool = ..., InternalCommunicationFault: bool = ..., InternalConversionFault: bool = ..., InternalLogicFault: bool = ..., InternalMemoryFault: bool = ..., InternalThermistorsFault: bool = ..., LowCellVoltageFault: bool = ..., OpenWiringFault: bool = ..., PackVoltageSensorFault: bool = ..., ThermistorFault: bool = ..., VoltageRedundancyFault: bool = ..., WeakCellFault: bool = ..., WeakPackFault: bool = ...) -> None: ...

class IBatteryLimitFlags(_message.Message):
    __slots__ = ("CclReducedDueToAlternateCurrentLimit", "CclReducedDueToChargerLatch", "CclReducedDueToHighCellResistance", "CclReducedDueToHighCellVoltage", "CclReducedDueToHighPackVoltage", "CclReducedDueToHighSoc", "CclReducedDueToTemperature", "DclReducedDueToHighCellResistance", "DclReducedDueToLowCellVoltage", "DclReducedDueToLowPackVoltage", "DclReducedDueToLowSoc", "DclReducedDueToTemperature", "DclandCclReducedDueToCommunicationFailsafe", "DclandCclReducedDueToVoltageFailsafe")
    CCLREDUCEDDUETOALTERNATECURRENTLIMIT_FIELD_NUMBER: _ClassVar[int]
    CCLREDUCEDDUETOCHARGERLATCH_FIELD_NUMBER: _ClassVar[int]
    CCLREDUCEDDUETOHIGHCELLRESISTANCE_FIELD_NUMBER: _ClassVar[int]
    CCLREDUCEDDUETOHIGHCELLVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    CCLREDUCEDDUETOHIGHPACKVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    CCLREDUCEDDUETOHIGHSOC_FIELD_NUMBER: _ClassVar[int]
    CCLREDUCEDDUETOTEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DCLREDUCEDDUETOHIGHCELLRESISTANCE_FIELD_NUMBER: _ClassVar[int]
    DCLREDUCEDDUETOLOWCELLVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    DCLREDUCEDDUETOLOWPACKVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    DCLREDUCEDDUETOLOWSOC_FIELD_NUMBER: _ClassVar[int]
    DCLREDUCEDDUETOTEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DCLANDCCLREDUCEDDUETOCOMMUNICATIONFAILSAFE_FIELD_NUMBER: _ClassVar[int]
    DCLANDCCLREDUCEDDUETOVOLTAGEFAILSAFE_FIELD_NUMBER: _ClassVar[int]
    CclReducedDueToAlternateCurrentLimit: bool
    CclReducedDueToChargerLatch: bool
    CclReducedDueToHighCellResistance: bool
    CclReducedDueToHighCellVoltage: bool
    CclReducedDueToHighPackVoltage: bool
    CclReducedDueToHighSoc: bool
    CclReducedDueToTemperature: bool
    DclReducedDueToHighCellResistance: bool
    DclReducedDueToLowCellVoltage: bool
    DclReducedDueToLowPackVoltage: bool
    DclReducedDueToLowSoc: bool
    DclReducedDueToTemperature: bool
    DclandCclReducedDueToCommunicationFailsafe: bool
    DclandCclReducedDueToVoltageFailsafe: bool
    def __init__(self, CclReducedDueToAlternateCurrentLimit: bool = ..., CclReducedDueToChargerLatch: bool = ..., CclReducedDueToHighCellResistance: bool = ..., CclReducedDueToHighCellVoltage: bool = ..., CclReducedDueToHighPackVoltage: bool = ..., CclReducedDueToHighSoc: bool = ..., CclReducedDueToTemperature: bool = ..., DclReducedDueToHighCellResistance: bool = ..., DclReducedDueToLowCellVoltage: bool = ..., DclReducedDueToLowPackVoltage: bool = ..., DclReducedDueToLowSoc: bool = ..., DclReducedDueToTemperature: bool = ..., DclandCclReducedDueToCommunicationFailsafe: bool = ..., DclandCclReducedDueToVoltageFailsafe: bool = ...) -> None: ...

class ICcs(_message.Message):
    __slots__ = ("CcsAlive",)
    CCSALIVE_FIELD_NUMBER: _ClassVar[int]
    CcsAlive: bool
    def __init__(self, CcsAlive: bool = ...) -> None: ...

class IMPPT(_message.Message):
    __slots__ = ("Alive", "ArrayCurrent", "ArrayVoltage", "BatteryVoltage", "Temperature")
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    ARRAYCURRENT_FIELD_NUMBER: _ClassVar[int]
    ARRAYVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    BATTERYVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    Alive: bool
    ArrayCurrent: float
    ArrayVoltage: float
    BatteryVoltage: float
    Temperature: float
    def __init__(self, Alive: bool = ..., ArrayCurrent: _Optional[float] = ..., ArrayVoltage: _Optional[float] = ..., BatteryVoltage: _Optional[float] = ..., Temperature: _Optional[float] = ...) -> None: ...

class IMotorFault(_message.Message):
    __slots__ = ("ErrorFlags", "LimitFlags", "RxErrorCount", "TxErrorCount")
    ERRORFLAGS_FIELD_NUMBER: _ClassVar[int]
    LIMITFLAGS_FIELD_NUMBER: _ClassVar[int]
    RXERRORCOUNT_FIELD_NUMBER: _ClassVar[int]
    TXERRORCOUNT_FIELD_NUMBER: _ClassVar[int]
    ErrorFlags: IMotorErrorFlags
    LimitFlags: IMotorLimitFlags
    RxErrorCount: int
    TxErrorCount: int
    def __init__(self, ErrorFlags: _Optional[_Union[IMotorErrorFlags, _Mapping]] = ..., LimitFlags: _Optional[_Union[IMotorLimitFlags, _Mapping]] = ..., RxErrorCount: _Optional[int] = ..., TxErrorCount: _Optional[int] = ...) -> None: ...

class IMotorErrorFlags(_message.Message):
    __slots__ = ("BadMotorPositionHallSequence", "ConfigReadError", "DcBusOverVoltage", "DesaturationFault", "MotorOverSpeed", "SoftwareOverCurrent", "Wail15VUnderVoltageLockOut", "WatchdogCausedLastReset")
    BADMOTORPOSITIONHALLSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CONFIGREADERROR_FIELD_NUMBER: _ClassVar[int]
    DCBUSOVERVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    DESATURATIONFAULT_FIELD_NUMBER: _ClassVar[int]
    MOTOROVERSPEED_FIELD_NUMBER: _ClassVar[int]
    SOFTWAREOVERCURRENT_FIELD_NUMBER: _ClassVar[int]
    WAIL15VUNDERVOLTAGELOCKOUT_FIELD_NUMBER: _ClassVar[int]
    WATCHDOGCAUSEDLASTRESET_FIELD_NUMBER: _ClassVar[int]
    BadMotorPositionHallSequence: bool
    ConfigReadError: bool
    DcBusOverVoltage: bool
    DesaturationFault: bool
    MotorOverSpeed: bool
    SoftwareOverCurrent: bool
    Wail15VUnderVoltageLockOut: bool
    WatchdogCausedLastReset: bool
    def __init__(self, BadMotorPositionHallSequence: bool = ..., ConfigReadError: bool = ..., DcBusOverVoltage: bool = ..., DesaturationFault: bool = ..., MotorOverSpeed: bool = ..., SoftwareOverCurrent: bool = ..., Wail15VUnderVoltageLockOut: bool = ..., WatchdogCausedLastReset: bool = ...) -> None: ...

class IMotorLimitFlags(_message.Message):
    __slots__ = ("BusCurrent", "BusVoltageLower", "BusVoltageUpper", "IpmOrMotorTemperature", "MotorCurrent", "OutputVoltagePwm", "Velocity")
    BUSCURRENT_FIELD_NUMBER: _ClassVar[int]
    BUSVOLTAGELOWER_FIELD_NUMBER: _ClassVar[int]
    BUSVOLTAGEUPPER_FIELD_NUMBER: _ClassVar[int]
    IPMORMOTORTEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MOTORCURRENT_FIELD_NUMBER: _ClassVar[int]
    OUTPUTVOLTAGEPWM_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    BusCurrent: bool
    BusVoltageLower: bool
    BusVoltageUpper: bool
    IpmOrMotorTemperature: bool
    MotorCurrent: bool
    OutputVoltagePwm: bool
    Velocity: bool
    def __init__(self, BusCurrent: bool = ..., BusVoltageLower: bool = ..., BusVoltageUpper: bool = ..., IpmOrMotorTemperature: bool = ..., MotorCurrent: bool = ..., OutputVoltagePwm: bool = ..., Velocity: bool = ...) -> None: ...

class IBattery(_message.Message):
    __slots__ = ("InputVoltage", "Alive", "AverageCellVoltage", "AverageTemperature", "BMSRelayStatusFlags", "FanSpeed", "FanVoltage", "HighCellVoltage", "HighCellVoltageId", "HighTemperature", "HighThermistorId", "InternalTemperature", "LowCellVoltage", "LowCellVoltageId", "LowTemperature", "LowThermistorId", "PackAmphours", "PackCurrent", "PackDepthOfDischarge", "PackStateOfCharge", "PackVoltage", "PopulatedCells", "RequestedFanSpeed")
    INPUTVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    AVERAGECELLVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    AVERAGETEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    BMSRELAYSTATUSFLAGS_FIELD_NUMBER: _ClassVar[int]
    FANSPEED_FIELD_NUMBER: _ClassVar[int]
    FANVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    HIGHCELLVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    HIGHCELLVOLTAGEID_FIELD_NUMBER: _ClassVar[int]
    HIGHTEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    HIGHTHERMISTORID_FIELD_NUMBER: _ClassVar[int]
    INTERNALTEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    LOWCELLVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    LOWCELLVOLTAGEID_FIELD_NUMBER: _ClassVar[int]
    LOWTEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    LOWTHERMISTORID_FIELD_NUMBER: _ClassVar[int]
    PACKAMPHOURS_FIELD_NUMBER: _ClassVar[int]
    PACKCURRENT_FIELD_NUMBER: _ClassVar[int]
    PACKDEPTHOFDISCHARGE_FIELD_NUMBER: _ClassVar[int]
    PACKSTATEOFCHARGE_FIELD_NUMBER: _ClassVar[int]
    PACKVOLTAGE_FIELD_NUMBER: _ClassVar[int]
    POPULATEDCELLS_FIELD_NUMBER: _ClassVar[int]
    REQUESTEDFANSPEED_FIELD_NUMBER: _ClassVar[int]
    InputVoltage: float
    Alive: bool
    AverageCellVoltage: float
    AverageTemperature: float
    BMSRelayStatusFlags: IBMSRelayStatusFlags
    FanSpeed: float
    FanVoltage: float
    HighCellVoltage: float
    HighCellVoltageId: int
    HighTemperature: float
    HighThermistorId: int
    InternalTemperature: float
    LowCellVoltage: float
    LowCellVoltageId: int
    LowTemperature: float
    LowThermistorId: int
    PackAmphours: float
    PackCurrent: float
    PackDepthOfDischarge: float
    PackStateOfCharge: float
    PackVoltage: float
    PopulatedCells: int
    RequestedFanSpeed: float
    def __init__(self, InputVoltage: _Optional[float] = ..., Alive: bool = ..., AverageCellVoltage: _Optional[float] = ..., AverageTemperature: _Optional[float] = ..., BMSRelayStatusFlags: _Optional[_Union[IBMSRelayStatusFlags, _Mapping]] = ..., FanSpeed: _Optional[float] = ..., FanVoltage: _Optional[float] = ..., HighCellVoltage: _Optional[float] = ..., HighCellVoltageId: _Optional[int] = ..., HighTemperature: _Optional[float] = ..., HighThermistorId: _Optional[int] = ..., InternalTemperature: _Optional[float] = ..., LowCellVoltage: _Optional[float] = ..., LowCellVoltageId: _Optional[int] = ..., LowTemperature: _Optional[float] = ..., LowThermistorId: _Optional[int] = ..., PackAmphours: _Optional[float] = ..., PackCurrent: _Optional[float] = ..., PackDepthOfDischarge: _Optional[float] = ..., PackStateOfCharge: _Optional[float] = ..., PackVoltage: _Optional[float] = ..., PopulatedCells: _Optional[int] = ..., RequestedFanSpeed: _Optional[float] = ...) -> None: ...

class IBMSRelayStatusFlags(_message.Message):
    __slots__ = ("AlwaysOnSignalStatus", "ChargeRelayEnabled", "ChargerSafetyEnabled", "DischargeRelayEnabled", "IsChargingSignalStatus", "IsReadySignalStatus", "MalfunctionIndicatorActive", "MultiPurposeInputSignalStatus")
    ALWAYSONSIGNALSTATUS_FIELD_NUMBER: _ClassVar[int]
    CHARGERELAYENABLED_FIELD_NUMBER: _ClassVar[int]
    CHARGERSAFETYENABLED_FIELD_NUMBER: _ClassVar[int]
    DISCHARGERELAYENABLED_FIELD_NUMBER: _ClassVar[int]
    ISCHARGINGSIGNALSTATUS_FIELD_NUMBER: _ClassVar[int]
    ISREADYSIGNALSTATUS_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONINDICATORACTIVE_FIELD_NUMBER: _ClassVar[int]
    MULTIPURPOSEINPUTSIGNALSTATUS_FIELD_NUMBER: _ClassVar[int]
    AlwaysOnSignalStatus: bool
    ChargeRelayEnabled: bool
    ChargerSafetyEnabled: bool
    DischargeRelayEnabled: bool
    IsChargingSignalStatus: bool
    IsReadySignalStatus: bool
    MalfunctionIndicatorActive: bool
    MultiPurposeInputSignalStatus: bool
    def __init__(self, AlwaysOnSignalStatus: bool = ..., ChargeRelayEnabled: bool = ..., ChargerSafetyEnabled: bool = ..., DischargeRelayEnabled: bool = ..., IsChargingSignalStatus: bool = ..., IsReadySignalStatus: bool = ..., MalfunctionIndicatorActive: bool = ..., MultiPurposeInputSignalStatus: bool = ...) -> None: ...
