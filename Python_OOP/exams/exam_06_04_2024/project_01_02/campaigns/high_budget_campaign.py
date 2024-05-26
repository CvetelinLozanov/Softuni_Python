from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, 5000, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        required_engagement = self.required_engagement * 1.20
        if engagement_rate >= required_engagement:
            return True
        return False
