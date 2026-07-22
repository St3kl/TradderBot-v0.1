from app.audit.signal_auditor import SignalAuditor
from app.audit.score_breakdown import ScoreBreakdown
from app.audit.rejection_analyzer import RejectionAnalyzer


class AuditEngine:

    def __init__(self):

        self.signal = SignalAuditor()

        self.score = ScoreBreakdown()

        self.reject = RejectionAnalyzer()

    def analyze(self, session):

        checklist = self.signal.audit(session)

        breakdown = self.score.calculate(

            checklist

        )

        rejected = self.reject.analyze(

            checklist

        )

        return {

            "checklist": checklist,

            "breakdown": breakdown,

            "rejected": rejected

        }