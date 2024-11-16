# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import callback_delete_all_subscriptions_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["CallbackResource", "AsyncCallbackResource"]


class CallbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return CallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return CallbackResourceWithStreamingResponse(self)

    def delete_all_subscriptions(
        self,
        *,
        description: str,
        status: Literal["Unsubscribe successful", "Unsubscribe unsuccessful"],
        status_code: int,
        subscription_id: int | NotGiven = NOT_GIVEN,
        subscription_provider_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The result of the asynchronous DELETE for all a customers subscriptions will be
        POSTed to the callback URL that the developer must host. If there were multiple
        subscriptions, each result will be posted individually as it completes.

        Args:
          description: Details of the result of the unsubscribe action

          status_code: Status Code

          subscription_id: ID for the Subscription

          subscription_provider_id: Identity of the subscription provider hosting the subscription

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/callback/delete-all-subscriptions",
            body=maybe_transform(
                {
                    "description": description,
                    "status": status,
                    "status_code": status_code,
                    "subscription_id": subscription_id,
                    "subscription_provider_id": subscription_provider_id,
                },
                callback_delete_all_subscriptions_params.CallbackDeleteAllSubscriptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCallbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncCallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return AsyncCallbackResourceWithStreamingResponse(self)

    async def delete_all_subscriptions(
        self,
        *,
        description: str,
        status: Literal["Unsubscribe successful", "Unsubscribe unsuccessful"],
        status_code: int,
        subscription_id: int | NotGiven = NOT_GIVEN,
        subscription_provider_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The result of the asynchronous DELETE for all a customers subscriptions will be
        POSTed to the callback URL that the developer must host. If there were multiple
        subscriptions, each result will be posted individually as it completes.

        Args:
          description: Details of the result of the unsubscribe action

          status_code: Status Code

          subscription_id: ID for the Subscription

          subscription_provider_id: Identity of the subscription provider hosting the subscription

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/callback/delete-all-subscriptions",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "status": status,
                    "status_code": status_code,
                    "subscription_id": subscription_id,
                    "subscription_provider_id": subscription_provider_id,
                },
                callback_delete_all_subscriptions_params.CallbackDeleteAllSubscriptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CallbackResourceWithRawResponse:
    def __init__(self, callback: CallbackResource) -> None:
        self._callback = callback

        self.delete_all_subscriptions = to_raw_response_wrapper(
            callback.delete_all_subscriptions,
        )


class AsyncCallbackResourceWithRawResponse:
    def __init__(self, callback: AsyncCallbackResource) -> None:
        self._callback = callback

        self.delete_all_subscriptions = async_to_raw_response_wrapper(
            callback.delete_all_subscriptions,
        )


class CallbackResourceWithStreamingResponse:
    def __init__(self, callback: CallbackResource) -> None:
        self._callback = callback

        self.delete_all_subscriptions = to_streamed_response_wrapper(
            callback.delete_all_subscriptions,
        )


class AsyncCallbackResourceWithStreamingResponse:
    def __init__(self, callback: AsyncCallbackResource) -> None:
        self._callback = callback

        self.delete_all_subscriptions = async_to_streamed_response_wrapper(
            callback.delete_all_subscriptions,
        )
