# environment.py

class KubernetesCluster:
    def __init__(self, size, ec2_instance_type):
        self.size = size
        self.ec2_instance_type = ec2_instance_type

    def configure(self):
        # Simulate configuring the Kubernetes cluster
        print(f"Configuring Kubernetes cluster - Size: {self.size}, EC2 Instance Type: {self.ec2_instance_type}")
