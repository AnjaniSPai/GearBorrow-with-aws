from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import DocumentDB
from diagrams.aws.storage import S3
from diagrams.programming.framework import Flask
from diagrams.programming.language import Python
from diagrams.onprem.client import User
from diagrams.onprem.database import MongoDB
from diagrams.generic.storage import Storage  # <--- THIS IS THE FIX

# Diagram title and background
diag_attr = {
    "fontsize": "20",
    "bgcolor": "white"
}

with Diagram("Cloud-Ready System Architecture: GearBorrow Platform", show=False, filename="gearborrow_architecture", graph_attr=diag_attr):
    # CLIENT LAYER
    user_clients = [User("Player (Renter)"), User("Administrator")]

    with Cluster("AWS Cloud Infrastructure (Logical Deployment)"):

        with Cluster("Compute Layer"):
            # FLASK APP 
            with Cluster("App Server Instance (e.g., EC2)"):
                flask_app = Flask("GearBorrow App (app.py)")
                python_runtime = Python("Python / Flask Runtime")
                # Showing they run together
                python_runtime - Edge(style="dashed", color="gray") - flask_app
        
        with Cluster("Data & Storage Layer"):
            # DATABASE (MongoDB)
            mongo_db = MongoDB("Mongo NoSQL Database\n(Users / Inventory / Receipts)")
            
            # STORAGE (Local File System fixed using generic Storage node)
            local_uploads = Storage("S3-Style Object Storage\n(static/uploads/)")

    # FLOW DEFINITION
    # Client communicates with the Flask server
    user_clients >> Edge(color="blue", label="HTTP Requests (GET/POST)") >> flask_app
    
    # Server talks to the database
    flask_app >> Edge(color="purple", label="PyMongo (CRUD Data)") >> mongo_db
    
    # Server saves uploaded files
    flask_app >> Edge(color="orange", label="Admin Image Uploads") >> local_uploads

    # Optional: Showing how local concepts map to real AWS services
    with Cluster("AWS Alternatives (Future Scope)"):
        aws_db = DocumentDB("DocumentDB (MongoDB API)")
        aws_s3 = S3("S3 (Object Storage)")

    mongo_db - Edge(style="dotted", color="purple") >> aws_db
    local_uploads - Edge(style="dotted", color="orange") >> aws_s3