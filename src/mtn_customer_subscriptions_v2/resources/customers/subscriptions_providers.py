# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.customers.customer_subscription_provider import CustomerSubscriptionProvider

__all__ = ["SubscriptionsProvidersResource", "AsyncSubscriptionsProvidersResource"]


class SubscriptionsProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return SubscriptionsProvidersResourceWithStreamingResponse(self)

    def list(
        self,
        customer_id: str,
        *,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSubscriptionProvider:
        """
        Show the list of all Subscription providers that a customer may have
        subscriptions with

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return self._get(
            f"/customers/{customer_id}/subscriptions-providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSubscriptionProvider,
        )


class AsyncSubscriptionsProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return AsyncSubscriptionsProvidersResourceWithStreamingResponse(self)

    async def list(
        self,
        customer_id: str,
        *,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSubscriptionProvider:
        """
        Show the list of all Subscription providers that a customer may have
        subscriptions with

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return await self._get(
            f"/customers/{customer_id}/subscriptions-providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSubscriptionProvider,
        )


class SubscriptionsProvidersResourceWithRawResponse:
    def __init__(self, subscriptions_providers: SubscriptionsProvidersResource) -> None:
        self._subscriptions_providers = subscriptions_providers

        self.list = to_raw_response_wrapper(
            subscriptions_providers.list,
        )


class AsyncSubscriptionsProvidersResourceWithRawResponse:
    def __init__(self, subscriptions_providers: AsyncSubscriptionsProvidersResource) -> None:
        self._subscriptions_providers = subscriptions_providers

        self.list = async_to_raw_response_wrapper(
            subscriptions_providers.list,
        )


class SubscriptionsProvidersResourceWithStreamingResponse:
    def __init__(self, subscriptions_providers: SubscriptionsProvidersResource) -> None:
        self._subscriptions_providers = subscriptions_providers

        self.list = to_streamed_response_wrapper(
            subscriptions_providers.list,
        )


class AsyncSubscriptionsProvidersResourceWithStreamingResponse:
    def __init__(self, subscriptions_providers: AsyncSubscriptionsProvidersResource) -> None:
        self._subscriptions_providers = subscriptions_providers

        self.list = async_to_streamed_response_wrapper(
            subscriptions_providers.list,
        )
