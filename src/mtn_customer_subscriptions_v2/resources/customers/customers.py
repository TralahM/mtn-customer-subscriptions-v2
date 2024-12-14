# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .subscriptions_providers import (
    SubscriptionsProvidersResource,
    AsyncSubscriptionsProvidersResource,
    SubscriptionsProvidersResourceWithRawResponse,
    AsyncSubscriptionsProvidersResourceWithRawResponse,
    SubscriptionsProvidersResourceWithStreamingResponse,
    AsyncSubscriptionsProvidersResourceWithStreamingResponse,
)
from .subscriptions.subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def subscriptions_providers(self) -> SubscriptionsProvidersResource:
        return SubscriptionsProvidersResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def subscriptions_providers(self) -> AsyncSubscriptionsProvidersResource:
        return AsyncSubscriptionsProvidersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-customer-subscriptions-v2#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._customers.subscriptions)

    @cached_property
    def subscriptions_providers(self) -> SubscriptionsProvidersResourceWithRawResponse:
        return SubscriptionsProvidersResourceWithRawResponse(self._customers.subscriptions_providers)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._customers.subscriptions)

    @cached_property
    def subscriptions_providers(self) -> AsyncSubscriptionsProvidersResourceWithRawResponse:
        return AsyncSubscriptionsProvidersResourceWithRawResponse(self._customers.subscriptions_providers)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._customers.subscriptions)

    @cached_property
    def subscriptions_providers(self) -> SubscriptionsProvidersResourceWithStreamingResponse:
        return SubscriptionsProvidersResourceWithStreamingResponse(self._customers.subscriptions_providers)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._customers.subscriptions)

    @cached_property
    def subscriptions_providers(self) -> AsyncSubscriptionsProvidersResourceWithStreamingResponse:
        return AsyncSubscriptionsProvidersResourceWithStreamingResponse(self._customers.subscriptions_providers)
