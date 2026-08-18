with open("notes.txt","r") as f:
    for line in f:
        clean_line=line.strip()
        if not clean_line:
            continue
        print(clean_line)

#Output

'''
Amazon Elastic Compute Cloud (Amazon EC2) offers the broadest and deepest compute platform,
with over 1000 instances and choice of the latest processor, storage, networking, operating system,
and purchase model to help you best match the needs of your workload.
We are the first major cloud provider that supports Intel, AMD, and Arm processors, the only cloud with on-demand EC2 Mac instances, and the only cloud with 400 Gbps Ethernet networking.
We offer the best price performance for machine learning training, as well as the lowest cost per inference instances in the cloud. More SAP, high performance computing (HPC), ML, and Windows workloads run on AWS than any other cloud.
'''