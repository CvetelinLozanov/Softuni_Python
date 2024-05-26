from typing import List

from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign
from project.influencers.standard_influencer import StandardInfluencer
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign


class InfluencerManagerApp():

    INFLUENCERS = {'PremiumInfluencer': PremiumInfluencer, 'StandardInfluencer': StandardInfluencer}
    CAMPAIGNS = {'HighBudgetCampaign': HighBudgetCampaign, 'LowBudgetCampaign': LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):

        if influencer_type not in InfluencerManagerApp.INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        user = self.get_influencer(username)
        if user is not None:
            return f"{username} is already registered."

        self.influencers.append(self.INFLUENCERS[influencer_type](username, followers, engagement_rate))
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        campaign = self.get_campaign(campaign_id)

        if campaign is not None:
            return f"Campaign ID {campaign_id} has already been created."

        self.campaigns.append(self.CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement))
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self.get_influencer(influencer_username)
        campaign = self.get_campaign(campaign_id)

        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the eligibility criteria for"
                    f" the campaign with ID {campaign_id}.")

        influencer_payment = influencer.calculate_payment(campaign)
        if influencer_payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)
            return (f"Influencer '{influencer_username}' has successfully participated in the campaign with "
                    f"ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        dict = {}
        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                if campaign not in dict:
                    dict[campaign] = 0
                dict[campaign] += influencer.reached_followers(campaign.__class__.__name__)

        return dict

    def influencer_campaign_report(self, username: str):
        influencer = self.get_influencer(username)
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))

        result = ''
        result += '$$ Campaign Statistics $$\n'
        for campaign in sorted_campaigns:
            total_reached_followers = self.calculate_total_reached_followers()[campaign]
            result += (f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)},"
                       f" Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}\n")

        return result.strip()

    def get_influencer(self, name: str):
        influencers = [influencer for influencer in self.influencers if name == influencer.username]
        return influencers[0] if influencers else None

    def get_campaign(self, campaign_id: int):
        campaigns = [campaign for campaign in self.campaigns if campaign_id == campaign.campaign_id]
        return campaigns[0] if campaigns else None