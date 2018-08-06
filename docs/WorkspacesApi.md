# swagger_client.WorkspacesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspacesApi.md#create_workspace) | **PUT** /tf/workspace/{name} | 
[**describe_workspace**](WorkspacesApi.md#describe_workspace) | **GET** /tf/workspace/{name} | 
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **GET** /tf/workspaces | 


# **create_workspace**
> ResourceTfWorkspace create_workspace(name, terraform_workspace=terraform_workspace)



Create a Terraform workspace

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | A terraform workspace
terraform_workspace = swagger_client.ResourceTfWorkspace() # ResourceTfWorkspace | A terraform workspace (optional)

try:
    api_response = api_instance.create_workspace(name, terraform_workspace=terraform_workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A terraform workspace | 
 **terraform_workspace** | [**ResourceTfWorkspace**](ResourceTfWorkspace.md)| A terraform workspace | [optional] 

### Return type

[**ResourceTfWorkspace**](ResourceTfWorkspace.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_workspace**
> ResourceTfWorkspace describe_workspace(name)



Describe a terraform workspace

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | A terraform workspace

try:
    api_response = api_instance.describe_workspace(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->describe_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A terraform workspace | 

### Return type

[**ResourceTfWorkspace**](ResourceTfWorkspace.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> ResponseListTfWorkspaces list_workspaces()



List approved terraform workspaces

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_workspaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseListTfWorkspaces**](ResponseListTfWorkspaces.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

