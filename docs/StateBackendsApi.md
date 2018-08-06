# swagger_client.StateBackendsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_state_backend**](StateBackendsApi.md#create_state_backend) | **POST** /tf/state-backends | 
[**list_state_backends**](StateBackendsApi.md#list_state_backends) | **GET** /tf/state-backends | 
[**update_state_backend**](StateBackendsApi.md#update_state_backend) | **PUT** /tf/state-backend/{id} | 


# **create_state_backend**
> ResourceTfStateBackend create_state_backend(terraform_state_backend=terraform_state_backend)



Define a Terraform state backend

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
api_instance = swagger_client.StateBackendsApi(swagger_client.ApiClient(configuration))
terraform_state_backend = swagger_client.ResourceTfStateBackend() # ResourceTfStateBackend | A terraform state backend (optional)

try:
    api_response = api_instance.create_state_backend(terraform_state_backend=terraform_state_backend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateBackendsApi->create_state_backend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terraform_state_backend** | [**ResourceTfStateBackend**](ResourceTfStateBackend.md)| A terraform state backend | [optional] 

### Return type

[**ResourceTfStateBackend**](ResourceTfStateBackend.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_state_backends**
> ResponseListTfStateBackends list_state_backends()



List TF State Backends

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
api_instance = swagger_client.StateBackendsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_state_backends()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateBackendsApi->list_state_backends: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseListTfStateBackends**](ResponseListTfStateBackends.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_backend**
> ResourceTfStateBackend update_state_backend(id, terraform_state_backend=terraform_state_backend)



Define a Terraform state backend

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
api_instance = swagger_client.StateBackendsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a terraform state backend
terraform_state_backend = swagger_client.ResourceTfStateBackend() # ResourceTfStateBackend | A terraform state backend (optional)

try:
    api_response = api_instance.update_state_backend(id, terraform_state_backend=terraform_state_backend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateBackendsApi->update_state_backend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a terraform state backend | 
 **terraform_state_backend** | [**ResourceTfStateBackend**](ResourceTfStateBackend.md)| A terraform state backend | [optional] 

### Return type

[**ResourceTfStateBackend**](ResourceTfStateBackend.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

