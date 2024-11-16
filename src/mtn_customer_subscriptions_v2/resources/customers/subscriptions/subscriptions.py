# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.customers import (
    subscription_list_params,
    subscription_create_params,
    subscription_delete_params,
    subscription_retrieve_params,
)
from ....types.customers.unsubscribe import Unsubscribe
from ....types.customers.subscription import Subscription
from ....types.shared.customer_subscription import CustomerSubscription

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        customer_id: str,
        *,
        subscription_id: str,
        subscription_name: str,
        subscription_provider_id: str,
        auto_renew: bool | NotGiven = NOT_GIVEN,
        beneficiary_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        registration_channel: str | NotGiven = NOT_GIVEN,
        send_sms_notification: bool | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        subscription_description: str | NotGiven = NOT_GIVEN,
        subscription_length: str | NotGiven = NOT_GIVEN,
        subscription_payment_source: str | NotGiven = NOT_GIVEN,
        subscription_status: Literal["Active", "Inactive", "Pending"] | NotGiven = NOT_GIVEN,
        subscription_type: Literal["Adhoc", "Recurring"] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subscription:
        """
        Provision/add a new subscription to the customers account

        Args:
          subscription_id: Unique identifier for the Subscription

          subscription_name: Service the customer is subscribed to

          subscription_provider_id: Identifier for the provider within which the Subscription lives

          auto_renew: Recurring subscription to auto-renew at the end of the expiry period

          beneficiary_id: Subscription will be added to the beneficiary, but payment deducted from the
              main customerId

          email: Email address associated with the Subscription

          end_date: End date of the Subscription; full-date notation RFC 3339

          registration_channel: Channel through which the customer subscribed to the service

          send_sms_notification: Should an SMS be sent to the subscriber to inform them of the subscription

          start_date: Start date of the Subscription; full-date notation RFC 3339

          subscription_description: Description of the service the customer is subscribed to

          subscription_length: Duration of the subscription the customer is subscribed to

          subscription_payment_source: Which payment balance to use to pay: Airtime, MoMo, EVDS, Loyalty

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return self._post(
            f"/customers/{customer_id}/subscriptions",
            body=maybe_transform(
                {
                    "subscription_id": subscription_id,
                    "subscription_name": subscription_name,
                    "subscription_provider_id": subscription_provider_id,
                    "auto_renew": auto_renew,
                    "beneficiary_id": beneficiary_id,
                    "email": email,
                    "end_date": end_date,
                    "registration_channel": registration_channel,
                    "send_sms_notification": send_sms_notification,
                    "start_date": start_date,
                    "subscription_description": subscription_description,
                    "subscription_length": subscription_length,
                    "subscription_payment_source": subscription_payment_source,
                    "subscription_status": subscription_status,
                    "subscription_type": subscription_type,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    def retrieve(
        self,
        subscription_id: str,
        *,
        customer_id: str,
        subscription_provider_id: str,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSubscription:
        """
        Retrieve specific subscription details for a customer

        Args:
          subscription_provider_id: Identity of the subscription provider hosting the subscription

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return self._get(
            f"/customers/{customer_id}/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"subscription_provider_id": subscription_provider_id},
                    subscription_retrieve_params.SubscriptionRetrieveParams,
                ),
            ),
            cast_to=CustomerSubscription,
        )

    def list(
        self,
        customer_id: str,
        *,
        subscription_provider_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSubscription:
        """
        Get a Customer's Subscriptions given the Customer's id

        Args:
          subscription_provider_id: Subscription Provider to query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return self._get(
            f"/customers/{customer_id}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"subscription_provider_id": subscription_provider_id},
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            cast_to=CustomerSubscription,
        )

    def delete(
        self,
        subscription_id: str,
        *,
        customer_id: str,
        subscription_provider_id: str,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Unsubscribe:
        """
        Delete a specific subscription

        Args:
          subscription_provider_id: Identity of the subscription provider hosting the subscription

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return self._delete(
            f"/customers/{customer_id}/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"subscription_provider_id": subscription_provider_id},
                    subscription_delete_params.SubscriptionDeleteParams,
                ),
            ),
            cast_to=Unsubscribe,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        customer_id: str,
        *,
        subscription_id: str,
        subscription_name: str,
        subscription_provider_id: str,
        auto_renew: bool | NotGiven = NOT_GIVEN,
        beneficiary_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        registration_channel: str | NotGiven = NOT_GIVEN,
        send_sms_notification: bool | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        subscription_description: str | NotGiven = NOT_GIVEN,
        subscription_length: str | NotGiven = NOT_GIVEN,
        subscription_payment_source: str | NotGiven = NOT_GIVEN,
        subscription_status: Literal["Active", "Inactive", "Pending"] | NotGiven = NOT_GIVEN,
        subscription_type: Literal["Adhoc", "Recurring"] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subscription:
        """
        Provision/add a new subscription to the customers account

        Args:
          subscription_id: Unique identifier for the Subscription

          subscription_name: Service the customer is subscribed to

          subscription_provider_id: Identifier for the provider within which the Subscription lives

          auto_renew: Recurring subscription to auto-renew at the end of the expiry period

          beneficiary_id: Subscription will be added to the beneficiary, but payment deducted from the
              main customerId

          email: Email address associated with the Subscription

          end_date: End date of the Subscription; full-date notation RFC 3339

          registration_channel: Channel through which the customer subscribed to the service

          send_sms_notification: Should an SMS be sent to the subscriber to inform them of the subscription

          start_date: Start date of the Subscription; full-date notation RFC 3339

          subscription_description: Description of the service the customer is subscribed to

          subscription_length: Duration of the subscription the customer is subscribed to

          subscription_payment_source: Which payment balance to use to pay: Airtime, MoMo, EVDS, Loyalty

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return await self._post(
            f"/customers/{customer_id}/subscriptions",
            body=await async_maybe_transform(
                {
                    "subscription_id": subscription_id,
                    "subscription_name": subscription_name,
                    "subscription_provider_id": subscription_provider_id,
                    "auto_renew": auto_renew,
                    "beneficiary_id": beneficiary_id,
                    "email": email,
                    "end_date": end_date,
                    "registration_channel": registration_channel,
                    "send_sms_notification": send_sms_notification,
                    "start_date": start_date,
                    "subscription_description": subscription_description,
                    "subscription_length": subscription_length,
                    "subscription_payment_source": subscription_payment_source,
                    "subscription_status": subscription_status,
                    "subscription_type": subscription_type,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    async def retrieve(
        self,
        subscription_id: str,
        *,
        customer_id: str,
        subscription_provider_id: str,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSubscription:
        """
        Retrieve specific subscription details for a customer

        Args:
          subscription_provider_id: Identity of the subscription provider hosting the subscription

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return await self._get(
            f"/customers/{customer_id}/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"subscription_provider_id": subscription_provider_id},
                    subscription_retrieve_params.SubscriptionRetrieveParams,
                ),
            ),
            cast_to=CustomerSubscription,
        )

    async def list(
        self,
        customer_id: str,
        *,
        subscription_provider_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSubscription:
        """
        Get a Customer's Subscriptions given the Customer's id

        Args:
          subscription_provider_id: Subscription Provider to query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return await self._get(
            f"/customers/{customer_id}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"subscription_provider_id": subscription_provider_id},
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            cast_to=CustomerSubscription,
        )

    async def delete(
        self,
        subscription_id: str,
        *,
        customer_id: str,
        subscription_provider_id: str,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Unsubscribe:
        """
        Delete a specific subscription

        Args:
          subscription_provider_id: Identity of the subscription provider hosting the subscription

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return await self._delete(
            f"/customers/{customer_id}/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"subscription_provider_id": subscription_provider_id},
                    subscription_delete_params.SubscriptionDeleteParams,
                ),
            ),
            cast_to=Unsubscribe,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            subscriptions.delete,
        )

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._subscriptions.status)


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subscriptions.delete,
        )

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._subscriptions.status)


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            subscriptions.delete,
        )

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._subscriptions.status)


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscriptions.delete,
        )

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._subscriptions.status)
