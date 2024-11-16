# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mtn_customer_subscriptions_v2 import MtnCustomerSubscriptionsV2, AsyncMtnCustomerSubscriptionsV2
from mtn_customer_subscriptions_v2.types.shared import CustomerSubscription

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MtnCustomerSubscriptionsV2) -> None:
        status = client.customers.subscriptions.status.retrieve(
            status_id="statusId",
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_provider_id="subscriptionProviderId",
        )
        assert_matches_type(CustomerSubscription, status, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: MtnCustomerSubscriptionsV2) -> None:
        status = client.customers.subscriptions.status.retrieve(
            status_id="statusId",
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_provider_id="subscriptionProviderId",
            transaction_id="transactionId",
        )
        assert_matches_type(CustomerSubscription, status, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MtnCustomerSubscriptionsV2) -> None:
        response = client.customers.subscriptions.status.with_raw_response.retrieve(
            status_id="statusId",
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_provider_id="subscriptionProviderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(CustomerSubscription, status, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MtnCustomerSubscriptionsV2) -> None:
        with client.customers.subscriptions.status.with_streaming_response.retrieve(
            status_id="statusId",
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_provider_id="subscriptionProviderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(CustomerSubscription, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.subscriptions.status.with_raw_response.retrieve(
                status_id="statusId",
                customer_id="",
                subscription_id="subscriptionId",
                subscription_provider_id="subscriptionProviderId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.customers.subscriptions.status.with_raw_response.retrieve(
                status_id="statusId",
                customer_id="customerId",
                subscription_id="",
                subscription_provider_id="subscriptionProviderId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            client.customers.subscriptions.status.with_raw_response.retrieve(
                status_id="",
                customer_id="customerId",
                subscription_id="subscriptionId",
                subscription_provider_id="subscriptionProviderId",
            )


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        status = await async_client.customers.subscriptions.status.retrieve(
            status_id="statusId",
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_provider_id="subscriptionProviderId",
        )
        assert_matches_type(CustomerSubscription, status, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        status = await async_client.customers.subscriptions.status.retrieve(
            status_id="statusId",
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_provider_id="subscriptionProviderId",
            transaction_id="transactionId",
        )
        assert_matches_type(CustomerSubscription, status, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        response = await async_client.customers.subscriptions.status.with_raw_response.retrieve(
            status_id="statusId",
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_provider_id="subscriptionProviderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(CustomerSubscription, status, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        async with async_client.customers.subscriptions.status.with_streaming_response.retrieve(
            status_id="statusId",
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_provider_id="subscriptionProviderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(CustomerSubscription, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.subscriptions.status.with_raw_response.retrieve(
                status_id="statusId",
                customer_id="",
                subscription_id="subscriptionId",
                subscription_provider_id="subscriptionProviderId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.customers.subscriptions.status.with_raw_response.retrieve(
                status_id="statusId",
                customer_id="customerId",
                subscription_id="",
                subscription_provider_id="subscriptionProviderId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            await async_client.customers.subscriptions.status.with_raw_response.retrieve(
                status_id="",
                customer_id="customerId",
                subscription_id="subscriptionId",
                subscription_provider_id="subscriptionProviderId",
            )
