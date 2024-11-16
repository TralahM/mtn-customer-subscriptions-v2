# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    subscription_id: Required[Annotated[str, PropertyInfo(alias="subscriptionId")]]
    """Unique identifier for the Subscription"""

    subscription_name: Required[Annotated[str, PropertyInfo(alias="subscriptionName")]]
    """Service the customer is subscribed to"""

    subscription_provider_id: Required[Annotated[str, PropertyInfo(alias="subscriptionProviderId")]]
    """Identifier for the provider within which the Subscription lives"""

    auto_renew: Annotated[bool, PropertyInfo(alias="auto-renew")]
    """Recurring subscription to auto-renew at the end of the expiry period"""

    beneficiary_id: Annotated[str, PropertyInfo(alias="beneficiaryId")]
    """
    Subscription will be added to the beneficiary, but payment deducted from the
    main customerId
    """

    email: str
    """Email address associated with the Subscription"""

    end_date: Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]
    """End date of the Subscription; full-date notation RFC 3339"""

    registration_channel: Annotated[str, PropertyInfo(alias="registrationChannel")]
    """Channel through which the customer subscribed to the service"""

    send_sms_notification: Annotated[bool, PropertyInfo(alias="sendSMSNotification")]
    """Should an SMS be sent to the subscriber to inform them of the subscription"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Start date of the Subscription; full-date notation RFC 3339"""

    subscription_description: Annotated[str, PropertyInfo(alias="subscriptionDescription")]
    """Description of the service the customer is subscribed to"""

    subscription_length: Annotated[str, PropertyInfo(alias="subscriptionLength")]
    """Duration of the subscription the customer is subscribed to"""

    subscription_payment_source: Annotated[str, PropertyInfo(alias="subscriptionPaymentSource")]
    """Which payment balance to use to pay: Airtime, MoMo, EVDS, Loyalty"""

    subscription_status: Annotated[Literal["Active", "Inactive", "Pending"], PropertyInfo(alias="subscriptionStatus")]

    subscription_type: Annotated[Literal["Adhoc", "Recurring"], PropertyInfo(alias="subscriptionType")]

    transaction_id: Annotated[str, PropertyInfo(alias="transactionId")]
