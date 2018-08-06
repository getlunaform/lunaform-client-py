# swagger_client.StacksApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_stack**](StacksApi.md#deploy_stack) | **POST** /tf/stacks | 
[**get_stack**](StacksApi.md#get_stack) | **GET** /tf/stack/{id} | 
[**list_deployments**](StacksApi.md#list_deployments) | **GET** /tf/stack/{id}/deployments | 
[**list_stacks**](StacksApi.md#list_stacks) | **GET** /tf/stacks | 
[**undeploy_stack**](StacksApi.md#undeploy_stack) | **DELETE** /tf/stack/{id} | 


# **deploy_stack**
> ResourceTfStack deploy_stack(terraform_stack=terraform_stack)



Deploy a stack from a module

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-lunaform-auth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-lunaform-auth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
terraform_stack = swagger_client.ResourceTfStack() # ResourceTfStack | A deployed terraform module (optional)

try:
    api_response = api_instance.deploy_stack(terraform_stack=terraform_stack)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->deploy_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terraform_stack** | [**ResourceTfStack**](ResourceTfStack.md)| A deployed terraform module | [optional] 

### Return type

[**ResourceTfStack**](ResourceTfStack.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack**
> ResourceTfStack get_stack(id)



Get a stack

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-lunaform-auth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-lunaform-auth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique identifier for this stack

try:
    api_response = api_instance.get_stack(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->get_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for this stack | 

### Return type

[**ResourceTfStack**](ResourceTfStack.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments**
> ResponseListTfDeployments list_deployments(id)



List the deployments for this stack

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-lunaform-auth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-lunaform-auth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique identifier for this stack

try:
    api_response = api_instance.list_deployments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->list_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for this stack | 

### Return type

[**ResponseListTfDeployments**](ResponseListTfDeployments.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stacks**
> ResponseListTfStacks list_stacks()



List deployed TF modules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-lunaform-auth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-lunaform-auth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_stacks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->list_stacks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseListTfStacks**](ResponseListTfStacks.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undeploy_stack**
> undeploy_stack(id)



Undeploy a teraform module

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-lunaform-auth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-lunaform-auth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique identifier for this stack

try:
    api_instance.undeploy_stack(id)
except ApiException as e:
    print("Exception when calling StacksApi->undeploy_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for this stack | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

