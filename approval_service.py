# approval_service.py
class ApprovalService:
    def approve_request(self, user_id, request_type, reason):
        # Simulate approving the request
        print(f"Approving request for User ID: {user_id}, Type: {request_type}, Reason: {reason}")
        return {'status': 'approved'}
