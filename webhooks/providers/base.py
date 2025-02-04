# providers/base.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict, Any
from django.http import HttpRequest  # Заменяем flask.Request на django.http.HttpRequest


class WebhookValidationError(Exception):
    """Raised when webhook validation fails"""
    pass


class WebhookError(Exception):
    """Base class for webhook errors"""
    pass


class InvalidDataError(WebhookError):
    """Raised when webhook data is invalid"""
    pass


class CustomerNotFoundError(WebhookError):
    """Raised when customer data cannot be found"""
    pass


class APIError(Exception):
    """Raised when API request fails"""
    pass


class InvalidEventType(WebhookError):
    """Raised when event type is not supported"""
    pass


@dataclass
class CustomerData:
    id: str
    email: str
    name: str
    created_at: datetime
    subscription_status: Optional[str] = None
    subscription_id: Optional[str] = None
    trial_end_date: Optional[datetime] = None
    payment_method: Optional[str] = None
    tags: Optional[List[str]] = None


@dataclass
class SubscriptionData:
    id: str
    status: str
    plan_name: str
    created_at: datetime
    trial_end_date: Optional[datetime] = None
    next_billing_date: Optional[datetime] = None
    amount: Optional[float] = None
    currency: Optional[str] = None


@dataclass
class PaymentEvent:
    id: str
    event_type: str
    customer_id: str
    amount: float
    currency: str
    status: str
    timestamp: datetime
    subscription_id: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None


class PaymentProvider(ABC):
    """Base class for payment providers"""

    def __init__(self, webhook_secret: str):
        self.webhook_secret = webhook_secret

    @abstractmethod
    def validate_webhook(self, request: HttpRequest) -> bool:
        """Validate webhook signature"""
        pass

    @abstractmethod
    def parse_webhook(self, request: HttpRequest, **kwargs) -> Optional[Dict[str, Any]]:
        """Parse webhook data"""
        pass

    def get_payment_history(self, customer_id: str) -> List[Dict[str, Any]]:
        """Get payment history for a customer"""
        return []

    def get_usage_metrics(self, customer_id: str) -> Dict[str, Any]:
        """Get usage metrics for a customer"""
        return {}

    def get_customer_data(self, customer_id: str) -> Dict[str, Any]:
        """Get customer data"""
        return {}

    def get_related_events(self, customer_id: str) -> List[Dict[str, Any]]:
        """Get related events for a customer"""
        return []