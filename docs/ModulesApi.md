# swagger_client.ModulesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_module**](ModulesApi.md#create_module) | **POST** /tf/modules | 
[**delete_module**](ModulesApi.md#delete_module) | **DELETE** /tf/module/{id} | 
[**get_module**](ModulesApi.md#get_module) | **GET** /tf/module/{id} | 
[**list_modules**](ModulesApi.md#list_modules) | **GET** /tf/modules | 


# **create_module**
> ResourceTfModule create_module(terraform_module=terraform_module)



Upload a Terraform module

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
api_instance = swagger_client.ModulesApi(swagger_client.ApiClient(configuration))
terraform_module = swagger_client.ResourceTfModule() # ResourceTfModule | A terraform module (optional)

try:
    api_response = api_instance.create_module(terraform_module=terraform_module)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModulesApi->create_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terraform_module** | [**ResourceTfModule**](ResourceTfModule.md)| A terraform module | [optional] 

### Return type

[**ResourceTfModule**](ResourceTfModule.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_module**
> delete_module(id)



Delete a terraform module

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
api_instance = swagger_client.ModulesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique identifier for this module

try:
    api_instance.delete_module(id)
except ApiException as e:
    print("Exception when calling ModulesApi->delete_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for this module | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_module**
> ResourceTfModule get_module(id)



Get a Terraform module

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
api_instance = swagger_client.ModulesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique identifier for this module

try:
    api_response = api_instance.get_module(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModulesApi->get_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for this module | 

### Return type

[**ResourceTfModule**](ResourceTfModule.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_modules**
> ResponseListTfModules list_modules()



List TF modules

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
api_instance = swagger_client.ModulesApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_modules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModulesApi->list_modules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseListTfModules**](ResponseListTfModules.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

