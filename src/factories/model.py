from typing import Dict, Any, Type
from abstractions import IFactory
from constants import Model
from models import Activity
from models import ActivityTypeLK
from models import AIScreeningConfig
from models import AIScreeningCriteria
from models import AIScreeningEvaluation
from models import AIScreeningRun
from models import AIScreeningStatusLK
from models import Application
from models import ApplicationPipeline
from models import AuthTypeLK
from models import AutomationRule
from models import BackgroundCheck
from models import BoardPosting
from models import Campaign
from models import CampaignStep
from models import Candidate
from models import CandidateLink
from models import CandidateLocation
from models import CandidateSkill
from models import CandidateTag
from models import CandidateUpload
from models import CareerConfig
from models import CountryLK
from models import CurrencyLK
from models import DedupGroup
from models import DedupGroupCandidate
from models import ESignature
from models import EmploymentConfig
from models import EmploymentTypeLK
from models import Enrollment
from models import Integration
from models import Interview
from models import InterviewInterviewer
from models import InterviewKit
from models import Job
from models import JobDomainLK
from models import JobInterviewPlan
from models import JobInterviewPlanInterviewer
from models import JobLocation
from models import JobRole
from models import JobRoleLevelLK
from models import JobSkill
from models import JobStage
from models import LocationLK
from models import MFATypeLK
from models import Notification
from models import Offer
from models import OtpTypeLK
from models import PortalApplication
from models import RatingLK
from models import RecommendationLK
from models import Requisition
from models import RequisitionApproval
from models import RuleRun
from models import SavedReport
from models import SchedulingLink
from models import SchedulingLinkInterviewer
from models import Scorecard
from models import ScorecardAttribute
from models import SkillLK
from models import SourcedProfile
from models import SourcedProfileSkill
from models import StageConfig
from models import Template
from models import TemplateTypeLK
from models import Tenant
from models import TenantProfile
from models import UploadTypeLK
from models import User
from models import UserOtp
from models import UserRecoveryCode
from models import UserTypeLK


class ModelFactory(IFactory[Any]):
    _registry: Dict[str, Type[Any]] = {
        Model.TENANT: Tenant,
        Model.TENANT_PROFILE: TenantProfile,
        Model.USER: User,
        Model.USER_OTP: UserOtp,
        Model.USER_RECOVERY_CODE: UserRecoveryCode,
        Model.USER_TYPE_LK: UserTypeLK,
    }

    def get(self, model_name: str, **overrides: Any) -> Any:
        key = model_name.lower()

        if key not in self._registry:
            raise KeyError(
                f"Unknown model name: '{model_name}'. Available: {list(self._registry.keys())}"
            )
        model_cls = self._registry[key]

        return model_cls(**overrides)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ModelFactory"
