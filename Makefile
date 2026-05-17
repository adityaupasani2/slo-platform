.PHONY: cluster-start cluster-stop deploy-monitoring deploy-app port-forward clean

cluster-start:
	minikube start --cpus=4 --memory=8192 --driver=docker

cluster-stop:
	minikube stop

deploy-monitoring:
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm repo update
	helm upgrade --install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
		-f k8s/monitoring/values.yaml \
		--namespace monitoring \
		--create-namespace

deploy-app:
	kubectl apply -f k8s/app/

port-forward:
	kubectl port-forward svc/kube-prometheus-stack-grafana 3000:80 -n monitoring &
	kubectl port-forward svc/kube-prometheus-stack-prometheus 9090:9090 -n monitoring &

clean:
	minikube delete