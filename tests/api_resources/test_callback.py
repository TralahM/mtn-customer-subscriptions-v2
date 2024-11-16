# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mtn_customer_subscriptions_v2 import MtnCustomerSubscriptionsV2, AsyncMtnCustomerSubscriptionsV2

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete_all_subscriptions(self, client: MtnCustomerSubscriptionsV2) -> None:
        callback = client.callback.delete_all_subscriptions(
            description="description",
            status="Unsubscribe successful",
            status_code=0,
        )
        assert callback is None

    @parametrize
    def test_method_delete_all_subscriptions_with_all_params(self, client: MtnCustomerSubscriptionsV2) -> None:
        callback = client.callback.delete_all_subscriptions(
            description="description",
            status="Unsubscribe successful",
            status_code=0,
            subscription_id=0,
            subscription_provider_id=0,
        )
        assert callback is None

    @parametrize
    def test_raw_response_delete_all_subscriptions(self, client: MtnCustomerSubscriptionsV2) -> None:
        response = client.callback.with_raw_response.delete_all_subscriptions(
            description="description",
            status="Unsubscribe successful",
            status_code=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = response.parse()
        assert callback is None

    @parametrize
    def test_streaming_response_delete_all_subscriptions(self, client: MtnCustomerSubscriptionsV2) -> None:
        with client.callback.with_streaming_response.delete_all_subscriptions(
            description="description",
            status="Unsubscribe successful",
            status_code=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = response.parse()
            assert callback is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCallback:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete_all_subscriptions(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        callback = await async_client.callback.delete_all_subscriptions(
            description="description",
            status="Unsubscribe successful",
            status_code=0,
        )
        assert callback is None

    @parametrize
    async def test_method_delete_all_subscriptions_with_all_params(
        self, async_client: AsyncMtnCustomerSubscriptionsV2
    ) -> None:
        callback = await async_client.callback.delete_all_subscriptions(
            description="description",
            status="Unsubscribe successful",
            status_code=0,
            subscription_id=0,
            subscription_provider_id=0,
        )
        assert callback is None

    @parametrize
    async def test_raw_response_delete_all_subscriptions(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        response = await async_client.callback.with_raw_response.delete_all_subscriptions(
            description="description",
            status="Unsubscribe successful",
            status_code=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = await response.parse()
        assert callback is None

    @parametrize
    async def test_streaming_response_delete_all_subscriptions(
        self, async_client: AsyncMtnCustomerSubscriptionsV2
    ) -> None:
        async with async_client.callback.with_streaming_response.delete_all_subscriptions(
            description="description",
            status="Unsubscribe successful",
            status_code=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = await response.parse()
            assert callback is None

        assert cast(Any, response.is_closed) is True
