---
layout: post
title:  "code snippet test"
date:   2017-12-21
desc: "Quick test on writing code snippets in a blog post"
keywords: "Jalpc,Jekyll,gh-pages,website,blog,easy"
categories: [HTML]
tags: [Jalpc,Jekyll]
icon: icon-html
---

Kubernetes_VB_dn02

2019년 3월 13일 수요일

오후 12:45

 

Minikube로 VirtualBox_dn02 에서 k8s 구동

 

Minikube는 k8s를 로컬에서 쉽게 실행하는 도구입니다.

>매일 k8s를 사용하거나 개발하려는 사용자들을 위해 VM 이나 노트북에서 단일 노드 k8s 클러스터를 실행합니다.

 

> Minikube 설치

Linux

 

`정적 바이너리를 내려받아서 리눅스에 minikube를 설치 할 수 있습니다.`

 

or

 

 

<img src="file:///C:/Users/user/AppData/Local/Packages/Microsoft.Office.OneNote_8wekyb3d8bbwe/TempState/msohtmlclip/clip_image001.png" width="747" height="107" alt="[root@dn02 curl —Lo minikube kube—1inux-amd64 chmod +x minikube https : //storage.googleapis.com/minikube/releases/latest[mini * Total 100 38.2M * Received * Xferd Average Speed Dload Upload 8801k T ime Total T ime Spent 100 38.2M o o T ime Cur rent Left Speed :-- 8803k ">

 

Minikube 실행 파일을 경로에 추가하는 쉬운 방법은 다음과 같습니다.

 

 

<img src="file:///C:/Users/user/AppData/Local/Packages/Microsoft.Office.OneNote_8wekyb3d8bbwe/TempState/msohtmlclip/clip_image002.png" width="497" height="43" alt="[root@dn02 sudo cp minikube Jusr/local/bin ss rm minikube cm: remove regular file 'minikube'? y ">

 

<img src="file:///C:/Users/user/AppData/Local/Packages/Microsoft.Office.OneNote_8wekyb3d8bbwe/TempState/msohtmlclip/clip_image003.png" width="254" height="35">

 

<img src="file:///C:/Users/user/AppData/Local/Packages/Microsoft.Office.OneNote_8wekyb3d8bbwe/TempState/msohtmlclip/clip_image004.png" width="745" height="161" alt="[root&dn02 minikube start minikube vo .3S.O on linux (amd64) > Creating virtualbox VM (CPUs=2, Memory=204BMB, Disk=20000MB) Downloading Minikube ISO 184.42 MB/ 184.42 MB t 100.00* os ! Unable to start VM: create: precreate: VBoxManage not found. Make sure VirtualBox is inst alled and VBoxManage is in the path Make sure to install all necessary requirements, according to the documentation: hr-tee : / . sks s/ in ">

 

Kubectl 설치

 

 

 

<img src="file:///C:/Users/user/AppData/Local/Packages/Microsoft.Office.OneNote_8wekyb3d8bbwe/TempState/msohtmlclip/clip_image005.png" width="746" height="222" alt="(root@dn02 cat > / etc/ yum. repos. d/kubernetes.repo > (kubernetesJ > name=Kubernetes > 64 > enabled—I > gpgchec > repo _gpgcheck=l > https://packages.cloud.google > EOF [root@dn02 yum install —y kubectl Loaded plugins : fastestmirror Loading mirror speeds from cached host file ">

 

Kubectl version

 

<img src="file:///C:/Users/user/AppData/Local/Packages/Microsoft.Office.OneNote_8wekyb3d8bbwe/TempState/msohtmlclip/clip_image006.png" width="747" height="114" alt="[root@dn02 kubectl version Client Version: version. Info {Major: Minor: "13", Gitversion: "VI. 13.4", Gitcommit: "c27b913f ddd1a6c480c229191a087698aa92f0b1", Go Version: "gol. 11.5", Compiler: "gc Platform: The connection to the server localhost: 8080 was refused - did you specify the right host or p ort? ">

 
