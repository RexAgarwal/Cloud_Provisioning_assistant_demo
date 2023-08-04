# api_gateway.py

class ApiGateway:
    def __init__(self, user_management_service, environment_provisioning_service):
        self.user_management_service = user_management_service
        self.environment_provisioning_service = environment_provisioning_service

    def handle_request(self, request):
        # Authenticate user, validate request, and route to the appropriate microservice
        user_info = self.user_management_service.authenticate_user(request['username'], request['password'])
        user_id, role = user_info['user_id'], user_info['role']

        # Additional logic to validate the request and route it to the correct microservice
        if request['action'] == 'provision_environment':
            request['user_id'] = user_id
            return self.environment_provisioning_service.provision_environment(request)

        elif request['action'] == 'delete_environment':
            environment_id = request['environment_id']
            return self.environment_provisioning_service.delete_environment(environment_id)
