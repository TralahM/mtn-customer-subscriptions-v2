# Shared Types

```python
from mtn_customer_subscriptions_v2.types import CustomerSubscription
```

# Customers

## Subscriptions

Types:

```python
from mtn_customer_subscriptions_v2.types.customers import Subscription, Unsubscribe
```

Methods:

- <code title="post /customers/{customerId}/subscriptions">client.customers.subscriptions.<a href="./src/mtn_customer_subscriptions_v2/resources/customers/subscriptions/subscriptions.py">create</a>(customer_id, \*\*<a href="src/mtn_customer_subscriptions_v2/types/customers/subscription_create_params.py">params</a>) -> <a href="./src/mtn_customer_subscriptions_v2/types/customers/subscription.py">Subscription</a></code>
- <code title="get /customers/{customerId}/subscriptions/{subscriptionId}">client.customers.subscriptions.<a href="./src/mtn_customer_subscriptions_v2/resources/customers/subscriptions/subscriptions.py">retrieve</a>(subscription_id, \*, customer_id, \*\*<a href="src/mtn_customer_subscriptions_v2/types/customers/subscription_retrieve_params.py">params</a>) -> <a href="./src/mtn_customer_subscriptions_v2/types/shared/customer_subscription.py">CustomerSubscription</a></code>
- <code title="get /customers/{customerId}/subscriptions">client.customers.subscriptions.<a href="./src/mtn_customer_subscriptions_v2/resources/customers/subscriptions/subscriptions.py">list</a>(customer_id, \*\*<a href="src/mtn_customer_subscriptions_v2/types/customers/subscription_list_params.py">params</a>) -> <a href="./src/mtn_customer_subscriptions_v2/types/shared/customer_subscription.py">CustomerSubscription</a></code>
- <code title="delete /customers/{customerId}/subscriptions/{subscriptionId}">client.customers.subscriptions.<a href="./src/mtn_customer_subscriptions_v2/resources/customers/subscriptions/subscriptions.py">delete</a>(subscription_id, \*, customer_id, \*\*<a href="src/mtn_customer_subscriptions_v2/types/customers/subscription_delete_params.py">params</a>) -> <a href="./src/mtn_customer_subscriptions_v2/types/customers/unsubscribe.py">Unsubscribe</a></code>

### Status

Methods:

- <code title="get /customers/{customerId}/subscriptions/{subscriptionId}/status/{statusId}">client.customers.subscriptions.status.<a href="./src/mtn_customer_subscriptions_v2/resources/customers/subscriptions/status.py">retrieve</a>(status_id, \*, customer_id, subscription_id, \*\*<a href="src/mtn_customer_subscriptions_v2/types/customers/subscriptions/status_retrieve_params.py">params</a>) -> <a href="./src/mtn_customer_subscriptions_v2/types/shared/customer_subscription.py">CustomerSubscription</a></code>

## SubscriptionsProviders

Types:

```python
from mtn_customer_subscriptions_v2.types.customers import CustomerSubscriptionProvider
```

Methods:

- <code title="get /customers/{customerId}/subscriptions-providers">client.customers.subscriptions_providers.<a href="./src/mtn_customer_subscriptions_v2/resources/customers/subscriptions_providers.py">list</a>(customer_id) -> <a href="./src/mtn_customer_subscriptions_v2/types/customers/customer_subscription_provider.py">CustomerSubscriptionProvider</a></code>

# Callback

Methods:

- <code title="post /callback/delete-all-subscriptions">client.callback.<a href="./src/mtn_customer_subscriptions_v2/resources/callback.py">delete_all_subscriptions</a>(\*\*<a href="src/mtn_customer_subscriptions_v2/types/callback_delete_all_subscriptions_params.py">params</a>) -> None</code>
