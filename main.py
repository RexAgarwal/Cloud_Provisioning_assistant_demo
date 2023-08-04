# demo.py
from api_gateway import ApiGateway
from environment_provisioning_service import EnvironmentProvisioningService, EnvironmentFactory, KubernetesCluster
from quota_management_service import QuotaManagementService
from approval_service import ApprovalService
from environment_tracking_service import EnvironmentTrackingService, NotificationService
from user_management_service import UserManagementService
from persistence_service import PersistenceService
# from metrics_logging_service import MetricsLoggingService
from circuit_breaker import CircuitBreaker

# Circuit Breaker setup
max_failures = 3
reset_timeout = 10  # seconds
provisioning_service_circuit_breaker = CircuitBreaker(max_failures, reset_timeout)

# Initialize services
user_management_service = UserManagementService()
quota_management_service = QuotaManagementService(ApprovalService())
notification_service = NotificationService()
environment_tracking_service = EnvironmentTrackingService(notification_service)
persistence_service = PersistenceService()
# metrics_logging_service = MetricsLoggingService()

# Environment Factory
environment_factory = EnvironmentFactory()

# Environment Provisioning Service with Circuit Breaker
environment_provisioning_service = EnvironmentProvisioningService(quota_management_service, environment_factory)
environment_provisioning_service = provisioning_service_circuit_breaker.execute(EnvironmentProvisioningService, quota_management_service, environment_factory)

# ApiGateway
api_gateway = ApiGateway(user_management_service, environment_provisioning_service)

def demo_program():
    try:
        # Simulate a developer making a provisioning request
        request = {
            'username': 'Himanshu',
            'password': 'password',
            'action': 'provision_environment',
            'environment_type': 'Kubernetes Cluster',
            'size': 'two-node small',
            'ec2_instance_type': 't3.micro',
        }

        response = api_gateway.handle_request(request)
        print("Response:", response)

        # Simulate a developer making a delete request
        request = {
            'username': 'Himanshu',
            'password': 'password',
            'action': 'delete_environment',
            'environment_id': 'env123',
        }

        response = api_gateway.handle_request(request)
        print("Response:", response)

    except Exception as e:
        print('Error occurred:', e)


# Run the demo program
demo_program()
