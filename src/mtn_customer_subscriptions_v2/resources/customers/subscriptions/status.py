# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....types.customers.subscriptions import status_retrieve_params
from ....types.shared.customer_subscription import CustomerSubscription

__all__ = ["StatusResource", "AsyncStatusResource"]


class StatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return StatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return StatusResourceWithStreamingResponse(self)

    def retrieve(
        self,
        status_id: str,
        *,
        customer_id: str,
        subscription_id: str,
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
        For certain provisioning requests to add a new subscription, the response will
        be asynchronous, with a status of PENDING. Use this query to poll the final
        status of the provisioning, using the transactionID that was used for the
        original provisioning request.

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
        if not status_id:
            raise ValueError(f"Expected a non-empty value for `status_id` but received {status_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return self._get(
            f"/customers/{customer_id}/subscriptions/{subscription_id}/status/{status_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"subscription_provider_id": subscription_provider_id}, status_retrieve_params.StatusRetrieveParams
                ),
            ),
            cast_to=CustomerSubscription,
        )


class AsyncStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return AsyncStatusResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        status_id: str,
        *,
        customer_id: str,
        subscription_id: str,
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
        For certain provisioning requests to add a new subscription, the response will
        be asynchronous, with a status of PENDING. Use this query to poll the final
        status of the provisioning, using the transactionID that was used for the
        original provisioning request.

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
        if not status_id:
            raise ValueError(f"Expected a non-empty value for `status_id` but received {status_id!r}")
        extra_headers = {**strip_not_given({"transactionId": transaction_id}), **(extra_headers or {})}
        return await self._get(
            f"/customers/{customer_id}/subscriptions/{subscription_id}/status/{status_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"subscription_provider_id": subscription_provider_id}, status_retrieve_params.StatusRetrieveParams
                ),
            ),
            cast_to=CustomerSubscription,
        )


class StatusResourceWithRawResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.retrieve = to_raw_response_wrapper(
            status.retrieve,
        )


class AsyncStatusResourceWithRawResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.retrieve = async_to_raw_response_wrapper(
            status.retrieve,
        )


class StatusResourceWithStreamingResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.retrieve = to_streamed_response_wrapper(
            status.retrieve,
        )


class AsyncStatusResourceWithStreamingResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.retrieve = async_to_streamed_response_wrapper(
            status.retrieve,
        )
