# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionListParams"]


class SubscriptionListParams(TypedDict, total=False):
    subscription_provider_id: Annotated[str, PropertyInfo(alias="subscriptionProviderId")]
    """Subscription Provider to query"""

    transaction_id: Annotated[str, PropertyInfo(alias="transactionId")]
