from app.safety.circuit_breaker import CircuitBreaker

breaker = CircuitBreaker(max_failures=3)

breaker.print()

print()

breaker.record_failure()
breaker.record_failure()

breaker.print()

print()

breaker.record_failure()

breaker.print()

print()

print("Trading Allowed:", not breaker.is_open())

print()

breaker.reset()

breaker.print()