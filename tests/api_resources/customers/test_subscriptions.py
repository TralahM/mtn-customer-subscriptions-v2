# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mtn_customer_subscriptions_v2 import MtnCustomerSubscriptionsV2, AsyncMtnCustomerSubscriptionsV2
from mtn_customer_subscriptions_v2._utils import parse_datetime
from mtn_customer_subscriptions_v2.types.shared import CustomerSubscription
from mtn_customer_subscriptions_v2.types.customers import (
    Unsubscribe,
    Subscription,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscription = client.customers.subscriptions.create(
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_name="subscriptionName",
            subscription_provider_id="subscriptionProviderId",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscription = client.customers.subscriptions.create(
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_name="subscriptionName",
            subscription_provider_id="subscriptionProviderId",
            auto_renew=True,
            beneficiary_id="beneficiaryId",
            email="email",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            registration_channel="registrationChannel",
            send_sms_notification=True,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            subscription_description="subscriptionDescription",
            subscription_length="subscriptionLength",
            subscription_payment_source="subscriptionPaymentSource",
            subscription_status="Active",
            subscription_type="Adhoc",
            transaction_id="transactionId",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MtnCustomerSubscriptionsV2) -> None:
        response = client.customers.subscriptions.with_raw_response.create(
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_name="subscriptionName",
            subscription_provider_id="subscriptionProviderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MtnCustomerSubscriptionsV2) -> None:
        with client.customers.subscriptions.with_streaming_response.create(
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_name="subscriptionName",
            subscription_provider_id="subscriptionProviderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: MtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.subscriptions.with_raw_response.create(
                customer_id="",
                subscription_id="subscriptionId",
                subscription_name="subscriptionName",
                subscription_provider_id="subscriptionProviderId",
            )

    @parametrize
    def test_method_retrieve(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscription = client.customers.subscriptions.retrieve(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        )
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscription = client.customers.subscriptions.retrieve(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
            transaction_id="transactionId",
        )
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MtnCustomerSubscriptionsV2) -> None:
        response = client.customers.subscriptions.with_raw_response.retrieve(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MtnCustomerSubscriptionsV2) -> None:
        with client.customers.subscriptions.with_streaming_response.retrieve(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(CustomerSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.subscriptions.with_raw_response.retrieve(
                subscription_id="subscriptionId",
                customer_id="",
                subscription_provider_id="subscriptionProviderId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.customers.subscriptions.with_raw_response.retrieve(
                subscription_id="",
                customer_id="customerId",
                subscription_provider_id="subscriptionProviderId",
            )

    @parametrize
    def test_method_list(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscription = client.customers.subscriptions.list(
            customer_id="customerId",
        )
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscription = client.customers.subscriptions.list(
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
            transaction_id="transactionId",
        )
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MtnCustomerSubscriptionsV2) -> None:
        response = client.customers.subscriptions.with_raw_response.list(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MtnCustomerSubscriptionsV2) -> None:
        with client.customers.subscriptions.with_streaming_response.list(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(CustomerSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: MtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.subscriptions.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_delete(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscription = client.customers.subscriptions.delete(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        )
        assert_matches_type(Unsubscribe, subscription, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: MtnCustomerSubscriptionsV2) -> None:
        subscription = client.customers.subscriptions.delete(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
            transaction_id="transactionId",
        )
        assert_matches_type(Unsubscribe, subscription, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: MtnCustomerSubscriptionsV2) -> None:
        response = client.customers.subscriptions.with_raw_response.delete(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Unsubscribe, subscription, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: MtnCustomerSubscriptionsV2) -> None:
        with client.customers.subscriptions.with_streaming_response.delete(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Unsubscribe, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.subscriptions.with_raw_response.delete(
                subscription_id="subscriptionId",
                customer_id="",
                subscription_provider_id="subscriptionProviderId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.customers.subscriptions.with_raw_response.delete(
                subscription_id="",
                customer_id="customerId",
                subscription_provider_id="subscriptionProviderId",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscription = await async_client.customers.subscriptions.create(
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_name="subscriptionName",
            subscription_provider_id="subscriptionProviderId",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscription = await async_client.customers.subscriptions.create(
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_name="subscriptionName",
            subscription_provider_id="subscriptionProviderId",
            auto_renew=True,
            beneficiary_id="beneficiaryId",
            email="email",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            registration_channel="registrationChannel",
            send_sms_notification=True,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            subscription_description="subscriptionDescription",
            subscription_length="subscriptionLength",
            subscription_payment_source="subscriptionPaymentSource",
            subscription_status="Active",
            subscription_type="Adhoc",
            transaction_id="transactionId",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        response = await async_client.customers.subscriptions.with_raw_response.create(
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_name="subscriptionName",
            subscription_provider_id="subscriptionProviderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        async with async_client.customers.subscriptions.with_streaming_response.create(
            customer_id="customerId",
            subscription_id="subscriptionId",
            subscription_name="subscriptionName",
            subscription_provider_id="subscriptionProviderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.subscriptions.with_raw_response.create(
                customer_id="",
                subscription_id="subscriptionId",
                subscription_name="subscriptionName",
                subscription_provider_id="subscriptionProviderId",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscription = await async_client.customers.subscriptions.retrieve(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        )
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscription = await async_client.customers.subscriptions.retrieve(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
            transaction_id="transactionId",
        )
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        response = await async_client.customers.subscriptions.with_raw_response.retrieve(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        async with async_client.customers.subscriptions.with_streaming_response.retrieve(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(CustomerSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.subscriptions.with_raw_response.retrieve(
                subscription_id="subscriptionId",
                customer_id="",
                subscription_provider_id="subscriptionProviderId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.customers.subscriptions.with_raw_response.retrieve(
                subscription_id="",
                customer_id="customerId",
                subscription_provider_id="subscriptionProviderId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscription = await async_client.customers.subscriptions.list(
            customer_id="customerId",
        )
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscription = await async_client.customers.subscriptions.list(
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
            transaction_id="transactionId",
        )
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        response = await async_client.customers.subscriptions.with_raw_response.list(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(CustomerSubscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        async with async_client.customers.subscriptions.with_streaming_response.list(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(CustomerSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.subscriptions.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscription = await async_client.customers.subscriptions.delete(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        )
        assert_matches_type(Unsubscribe, subscription, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        subscription = await async_client.customers.subscriptions.delete(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
            transaction_id="transactionId",
        )
        assert_matches_type(Unsubscribe, subscription, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        response = await async_client.customers.subscriptions.with_raw_response.delete(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Unsubscribe, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        async with async_client.customers.subscriptions.with_streaming_response.delete(
            subscription_id="subscriptionId",
            customer_id="customerId",
            subscription_provider_id="subscriptionProviderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Unsubscribe, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMtnCustomerSubscriptionsV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.subscriptions.with_raw_response.delete(
                subscription_id="subscriptionId",
                customer_id="",
                subscription_provider_id="subscriptionProviderId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.customers.subscriptions.with_raw_response.delete(
                subscription_id="",
                customer_id="customerId",
                subscription_provider_id="subscriptionProviderId",
            )
