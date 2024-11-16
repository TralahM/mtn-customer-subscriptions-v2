# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Subscription"]


class Subscription(BaseModel):
    subscription_id: str = FieldInfo(alias="subscriptionId")
    """Unique identifier for the Subscription"""

    subscription_name: str = FieldInfo(alias="subscriptionName")
    """Service the customer is subscribed to"""

    subscription_provider_id: str = FieldInfo(alias="subscriptionProviderId")
    """Identifier for the provider within which the Subscription lives"""

    auto_renew: Optional[bool] = FieldInfo(alias="auto-renew", default=None)
    """Recurring subscription to auto-renew at the end of the expiry period"""

    beneficiary_id: Optional[str] = FieldInfo(alias="beneficiaryId", default=None)
    """
    Subscription will be added to the beneficiary, but payment deducted from the
    main customerId
    """

    email: Optional[str] = None
    """Email address associated with the Subscription"""

    end_date: Optional[datetime] = FieldInfo(alias="endDate", default=None)
    """End date of the Subscription; full-date notation RFC 3339"""

    registration_channel: Optional[str] = FieldInfo(alias="registrationChannel", default=None)
    """Channel through which the customer subscribed to the service"""

    send_sms_notification: Optional[bool] = FieldInfo(alias="sendSMSNotification", default=None)
    """Should an SMS be sent to the subscriber to inform them of the subscription"""

    start_date: Optional[datetime] = FieldInfo(alias="startDate", default=None)
    """Start date of the Subscription; full-date notation RFC 3339"""

    subscription_description: Optional[str] = FieldInfo(alias="subscriptionDescription", default=None)
    """Description of the service the customer is subscribed to"""

    subscription_length: Optional[str] = FieldInfo(alias="subscriptionLength", default=None)
    """Duration of the subscription the customer is subscribed to"""

    subscription_payment_source: Optional[str] = FieldInfo(alias="subscriptionPaymentSource", default=None)
    """Which payment balance to use to pay: Airtime, MoMo, EVDS, Loyalty"""

    subscription_status: Optional[Literal["Active", "Inactive", "Pending"]] = FieldInfo(
        alias="subscriptionStatus", default=None
    )

    subscription_type: Optional[Literal["Adhoc", "Recurring"]] = FieldInfo(alias="subscriptionType", default=None)
