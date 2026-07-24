from app.safety.emergency_kill_switch import EmergencyKillSwitch

switch = EmergencyKillSwitch()

switch.print()

print()

switch.activate("Maximum daily loss exceeded")

switch.print()

print()

print("Trading Allowed:", not switch.is_active())

print()

switch.deactivate()

switch.print()