# swagger_client.ResourcesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_resource_groups**](ResourcesApi.md#list_resource_groups) | **GET** / | 
[**list_resources**](ResourcesApi.md#list_resources) | **GET** /{group} | 


# **list_resource_groups**
> ResponseListResources list_resource_groups()



List the root resource groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()

try:
    api_response = api_instance.list_resource_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->list_resource_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseListResources**](ResponseListResources.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resources**
> ResponseListResources list_resources(group)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()
group = 'group_example' # str | Root level resources

try:
    api_response = api_instance.list_resources(group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->list_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Root level resources | 

### Return type

[**ResponseListResources**](ResponseListResources.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

