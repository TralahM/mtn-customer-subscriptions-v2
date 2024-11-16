# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionRetrieveParams"]


class SubscriptionRetrieveParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]

    subscription_provider_id: Required[Annotated[str, PropertyInfo(alias="subscriptionProviderId")]]
    """Identity of the subscription provider hosting the subscription"""

    transaction_id: Annotated[str, PropertyInfo(alias="transactionId")]
