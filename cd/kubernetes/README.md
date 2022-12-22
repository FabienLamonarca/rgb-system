# Kubernetes app

```
# Install all helm / manifest
kubectl kustomize --enable-helm . | kubectl apply -f -

# Delete all helm / manifest
kubectl kustomize --enable-helm . | kubectl delete -f -
```