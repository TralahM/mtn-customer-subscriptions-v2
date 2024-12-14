# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mtn_customer_subscriptions_v2 import MtnCustomerSubscriptionsV2, AsyncMtnCustomerSubscriptionsV2
from mtn_customer_subscriptions_v2.types.customers import CustomerSubscriptionProvider

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptionsProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscriptions_provider = client.customers.subscriptions_providers.list(
            customer_id="customerId",
        )
        assert_matches_type(CustomerSubscriptionProvider, subscriptions_provider, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscriptions_provider = client.customers.subscriptions_providers.list(
            customer_id="customerId",
            transaction_id="transactionId",
        )
        assert_matches_type(CustomerSubscriptionProvider, subscriptions_provider, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MtnCustomerSubscriptionsV2) -> None:
        response = client.customers.subscriptions_providers.with_raw_response.list(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriptions_provider = response.parse()
        assert_matches_type(CustomerSubscriptionProvider, subscriptions_provider, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MtnCustomerSubscriptionsV2) -> None:
        with client.customers.subscriptions_providers.with_streaming_response.list(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriptions_provider = response.parse()
            assert_matches_type(CustomerSubscriptionProvider, subscriptions_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: MtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.subscriptions_providers.with_raw_response.list(
                customer_id="",
            )


class TestAsyncSubscriptionsProviders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscriptions_provider = await async_client.customers.subscriptions_providers.list(
            customer_id="customerId",
        )
        assert_matches_type(CustomerSubscriptionProvider, subscriptions_provider, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscriptions_provider = await async_client.customers.subscriptions_providers.list(
            customer_id="customerId",
            transaction_id="transactionId",
        )
        assert_matches_type(CustomerSubscriptionProvider, subscriptions_provider, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        response = await async_client.customers.subscriptions_providers.with_raw_response.list(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriptions_provider = await response.parse()
        assert_matches_type(CustomerSubscriptionProvider, subscriptions_provider, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        async with async_client.customers.subscriptions_providers.with_streaming_response.list(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriptions_provider = await response.parse()
            assert_matches_type(CustomerSubscriptionProvider, subscriptions_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.subscriptions_providers.with_raw_response.list(
                customer_id="",
            )