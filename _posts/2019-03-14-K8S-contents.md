---
layout: post
title:  "Kubernetes 개념"
date:   2019-03-14-K8S-contents/2019-03-13
desc: "Quick test on writing code snippets in a blog post"
keywords: "Kubernetes,Kubernetes"
categories: [Kubernetes]
tags: [JS,Jekyll]
icon: icon-html
---

# **Kubernetes 개념**
---
<br>
## 클라우드의 IaaS, PaaS, SaaS 개념   
---
<br>
  
- IaaS (Infrastructure as a Service)  
  
  - 서버를 운영하기 위해서는 서버 자원, IP, Network, Storage, 전력 등등 인프라를 구축하기 위해 여러가지가 필요합니다.  
  
  - 이러한 것들을 가상의 환경에서 쉽고 편하게 이용할 수 있게 서비스 형태로 제공합니다.  
  
  - IasS를 서비스로 제공하기 위해 기존 서버 호스팅보다 H/W 확장성이 좋고 탄력적이며 빠른 제공을 할 수 있는 가상화 기술을 이용합니다.  
  
  - IasS는 PaaS, SaaS의 기반이 되는 기술입니다.  
  
- PaaS (Platform as a Service)  
  
  - 서비스를 개발 할 수 있는 안정적인 환경(Platform)과 그 환경을 이용하는 응용 프로그램을 개발 할 수 있는 API까지 제공하는 형태를 Paas라고 합니다.  
  
- SaaS (Software as a Service)  
  
  - Cloud환경에서 동작하는 응용프로그램을 서비스 형태로 제공하는 것을 SaaS라고 합니다.  
  
  - 예를들어, 메일 서비스를 들 수 있습니다.  
    사용자는 이 시스템이 무엇으로 이루어져 있고 어떻게 동작하고 있는지, 그리고 메일을 백업을 어떻게 하는지 알 필요가 없습니다.  
    서비스 형태로 원하는 단말기(PC, Smartphone 등)에서 메일을 주고 받으며, 필요하면 언제든지 공간도 늘려서 서비스를 받을 수 있기 때문입니다.  
  
<br>
![](/static/assets/img/blog/2019-03-14-K8S-contents/2019-03-14-17-54-11.png){: .wh90 .center}  
  
- 내가 다 준비한다 : On-premise 
  
- 바닥은 있어야지 : Iaas (Infrastructure as a Service)  
  
- 먹을거만 사자 : Paas (Platform as a Service)  
  
- 돈만 있으면 되지 : Saas (Software as a Service)  
  
<br>
![](/static/assets/img/blog/2019-03-14-K8S-contents/2019-03-14-19-09-35.png){: .wh90 .center}  
  
<br>
![](/static/assets/img/blog/2019-03-14-K8S-contents/2019-03-14-19-09-56.png){: .wh90 .center}  
  
<br>
- Container Orchestration이 왜 필요한가??  
  
  - 여러개까지는 컨테이너를 쉘 프로그래밍으로 관리가 가능하겠지만, 수십개, 수백개가 되면 어려움을 겪기 때문에 사용합니다.  
<br>
- Container Orchestration  
    
  - 변수를 통제하고 안정적인 서비스를 목표로 하는 운영계에서 단순한 방법이 아닌 보다 체계적으로 관리를 합니다.  
<br>
- Container Orchestration의 기능  
  
  - 스케줄링
  
  - Cluster 관리
  
  - 서비스 Discovery
  
  - 모니터링
  
  - 설정
  
<br>
![](/static/assets/img/blog/2019-03-14-K8S-contents/2019-03-14-19-42-25.png){: .wh80 .center}
<br>
  
## **K8S (Kubernetes) 란?**  
---

  - 컨테이너 오케스트레이터(실행 및 관리)
  
  - 다양한 클라우드 및 베어 메탈 환경 지원
  
  - Google Borg에서 시작되어 오픈소스화 됨
  
  - 100% Go 언어로 작성
  
<br>
- K8S 특징
  
  - Automatic binpackin  
	: 가용성에 대한 희생없이, 리소스 사용과 제약 사항을 기준으로 자동으로 컨테이너를 스케줄링한다.
  
  - Self-healing  
	: 자동로 문제가 발생한 노드의 커테이너를 대체 (룰 / 정책에 따른 헬스 체크)
  
  - Horizontal scaling  
	: CPU와 메모리와 같은 리소스 사용에 따라 자동으로 애플리케이션을 확장 경우에 따라서, 사용자 정의 측정 값을 기준으로한 동적인 확장 가능
  
  - Service discovery and Load balancing  
	: Container에 고유한 IP를 부여하고, 여러 개의 Container를 묶어 단일 Service로 부여하는 경우 단일 DNS name으로 접근하도록 로드 밸런싱을 제공
  
  - Automatic rollouts and rollbacks  
	: 다운타임 없이 애플리케이션의 새로운 버전 및 설정에 대한 롤아웃 / 롤백 가능
  
  - Secret and configuration management  
	: 애플리케이션의 secret과 configuration 정보를 이미지와 독립적으로 구분하여 별도의 이미지 재생성 없이 관리
  
  - Storage orchestration  
	: 소프트웨어 정의 저장장치(Software Defined Storage)를 기반으로 로컬, 외부 및 저장소 솔루션 등을 동일한방법으로 컨테이너에 마운트 할 수 있다.
  
  - Batch execution  
	: CI 워크로드와 같은 Batch성 작업 지원, crontab 형식으로 스케줄링도 가능
  
<br>
  
## **K8S Architecture**
---
<br>
![](/static/assets/img/blog/2019-03-14-K8S-contents/2019-03-14-19-53-23.png){: .wh70 .center}  
   
<br>
- K8S Master
  
  - API server
	: Cluster와 상호 작용을 위한 K8S API 서버 (kubectl, Web UI의 입력 값을 받는 역할)
  
  - Scheduler
	: Worker node에 있는 pod를 스케줄
  
  - Controller-Manager
	: Deployments나 Replication Controller 등 관리
  
  - etcd
    : Master cluster에서 K8S object 저장소로 사용
  
<br>
![](/static/assets/img/blog/2019-03-14-K8S-contents/2019-03-14-19-57-12.png){: .wh70 .center}
  
<br>
- Kubernetes Node
  
  - Container runtime
	: 컨테이너 실행을 위한 Docker Engine 포함
  
  - Kubelet
	: Master의 명령 수행을 위한 k8s 에이전트
  
  - Kube-proxy
	: 인바운드 또는 아웃바운드 트래픽에 대한 네트워크 프록시 담당
  
  - cAdvisor
    : Container Advisor 리소스 사용 / 성능 통계를 제공
  
<br>
![](/static/assets/img/blog/2019-03-14-K8S-contents/2019-03-14-19-58-57.png){: .wh70 .center}
  
<br>
## **K8S Object 종류**
---
  - Basic object 
    : Pod, Service, Volume, Namespace
		
  - Controllers
	: ReplicaSet, Replication Controller, Deployment, StatefulSets, DaemonSet, Garbage Collection, Jobs, CronJob
  
<br>
- Pod
  
  - Worker 노드에서 실행되는 컨테이너의 집합(하나의 Pod은 일반적으로 하나의 컨테이너 사용)
  
  - 하나의 Pod에는 한 개 이상의 서비스로 지정 될 수 있음
  
  - 각각의 Pod는 고유한 IP가 할당 됨(내부 IP)
  
  - 하나의 Pod내에서는 PID namespace, network 와 hostname을 공유
  
<br>
- Service
  
  - Label Selector로 선택하여 하나의 endpoint로 노출되는 Pod의 집합
  
  - 종류 : ClusterIP, NodePort, LoadBalancer, ExternalName
  
<br>
![](/static/assets/img/blog/2019-03-14-K8S-contents/2019-03-14-20-14-20.png){: .wh70 .center}
  
<br>
- Ingress
  
  - 서비스에 대한 L7(애플리케이션 레이어) 라우터 정의
  
  - 사용자가 직접 서비스에 접근하지 않고 Ingrss를 통해 접근
  
<br>
![](/static/assets/img/blog/2019-03-14-K8S-contents/2019-03-14-20-19-47.png){: .wh70 .center}
  
<br>
- ConfigMap
  
  - Pod에 담겨진 container에서 사용되는 구성 값(DB의 이름, DB의 IP정보, DB의 정보, API Host 정보 등)
  
- Secret
  
  - 컨테이너에서 읽혀지거나 사용되는 소량의 민감한 정보
  
  - 특수한 volume이 자동으로 연결되어 container에서 사용가능
  
  - 수동으로 secret을 생성하고 연결하여 사용 가능
  
  - Base64로 encoding 될 뿐 암호화 되지는 않음
  
  - Volume으로 연결된 File 형식 또는 환경 변수 형식으로 사용 가능

- Deployment Controller
  
  - Pod의 배포 및 관리에 사용
  
  - ReplicaSet을 자동으로 생성
  
  - Pod에 대한 rolling 업데이트 관리

- ReplicaSet
  
  - Replication Controller의 새로운 버전
  
  - 가용성과 확장성 보장
  
  - 사용자의 요청에 따른 Pod의 숫자를 유지하고 관리
  
  - 각각의 Pod가 필요로하는 정보 명세가 있는 template를 이용 
  
<br>
<br>
대략적으로 이와 같은 계층적인 구조이다.

                    Deployment Controller

            ReplicaSet A               ReplicaSet B            

         Pod 1,  Pod 2,   …        Pod X,   Pod Y,    …
  
<br>
- StatefulSet
  
  - Deployment와 유사하나 Pod별 고정된 identity (name, network id 등) 할당
  
- DaemonSet
  
  - 모든 Node에 배포되어 실행 (Node Selector로 정의하는 경우 일부 Node 실행)
  
  - Node 상태에 따른 Monitoring 용으로 주로 사용 (storage 관리, log 수집, daemon 등)
  
<br>
- Job
  
  - 특정 task 실행을 위해 하나 혹은 이상의 pod를 생성하고 실행
  
  - Pod가 실행 완료하는 것을 보장(실패 시 재시도, deadline 설정 가능)
  
  - Job 실행 시 Pod의 순차 실행 또는 동시 실행 가능
  
  - 모든 pod 실행이 완료 시 Job의 완료로 인식하고 사용한 Pod를 제거함
  
<br>
- Volume

  - Pod에 연결되어 디렉토리 형태로 데이터를 저장 할 수 있도록 제공
  
  - Pod의 container 들끼리 공유, pod와 Life-cycle이 동일하게 적용되어 pod 삭제 시 같이 사라짐

- Volume Type

  - emptyDir, hostPath, gcePersistentDisk, awsElasticBlockStore, azureFileVolume, azureDiskVolume
  
  - Nfs, iscsi, cephfs, gitRepo, secret, persistentVolumeClaim 등

- PersistentVolume

  - k8s 클러스터 관리자에 의해 제공된 저장소의 일부
  
  - Volume과 유사하지만 pod와 독립적인 life-cycle을 가짐
  
  - 사용자가 용량, 모드 등 필요한 정보와 함께 PVC(PersistentVolumeClaim)를 생성하면 이에 대응하는 PersistentVolume 가 연결됨
  
  - NFS, ISCSI 또는 Cloud Provider 특화된 storage system으로 제공

- Persistent Volume Type

  - GCEPersistentDisk, AWSElasticBlockStore, AzureFile, AzureDisk, NFS, iSCSI,
  
  - CephFS, Cinder, Gluesterfs, Vmware Photon 등
  
<br>
## **K8S Tool**
---
  - Kubectl
    : K8S 클러스터 관리자를 위한 CLI(command line interface) 도구

  - Kubeadm
	: 물리서버, 클라우드 서버 또는 가상머신에 K8S 클러스터 구성을 쉽게 할 수 있도록 도와주는 CLI 도구

  - Kubefed
	: 연합 클러스터 운영을 위한 CLI 도구

  - Minikube
	: 개발이나 테스트를 목적으로 개인 PC에서 단일 노드 K8S 클러스터를 쉽게 제공하는 도구(VirtualBox로 제공)

  - Dashboard
    : Web UI 기반의 K8S 대시보드
  
<br>
- K8S 3rd party tools

  - K8S char
  
    - 사전 정의된 K8S 리소스에 대한 패키지
  
	- 필요한 모든 manifest를 메타 데이터와 함께 구성한 일종의 템플릿
  
	- Linux에서 rpm이나 deb와 유사
  
	- Chart 저장소는 https://github.com/kubernetes/charts/ 참고

  - K8S Helm
  
  	- K8S chart 패키지 관리 (조회, 설치, 갱신 및 삭제)
  
    - Linux의 yum 또는 apt와 유사
  
	- Tiler ; K8S 클러스터 내부에 설치된 서버
  
	- Helm ; 외부에서 접근하는 클라이언트 

  - K8S
  
	- Docker Compose 사용자을 K8S 옮겨 올 수 있도록 도와주는 도구
  
	- Docker Compose 파일을 K8S object로 변환
  
    - http://kompose.io 참고
  
<br>
