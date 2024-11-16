# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CustomerSubscription"]


class CustomerSubscription(BaseModel):
    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    services: Optional[object] = None
