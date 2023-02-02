#!/bin/bash

# delete existing resources first
kubectl kustomize --enable-helm . | kubectl delete -f -

# create all resources
kubectl kustomize --enable-helm . | kubectl apply -f -