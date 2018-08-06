# swagger_client.ProvidersApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provider**](ProvidersApi.md#create_provider) | **POST** /tf/providers/ | 
[**create_provider_configuration**](ProvidersApi.md#create_provider_configuration) | **POST** /tf/provider/{provider-name}/configurations | 
[**delete_provider**](ProvidersApi.md#delete_provider) | **DELETE** /tf/provider/{name} | 
[**delete_provider_configuration**](ProvidersApi.md#delete_provider_configuration) | **DELETE** /tf/provider/{provider-name}/configuration/{id} | 
[**get_provider**](ProvidersApi.md#get_provider) | **GET** /tf/provider/{name} | 
[**get_provider_configuration**](ProvidersApi.md#get_provider_configuration) | **GET** /tf/provider/{provider-name}/configuration/{id} | 
[**list_provider_configurations**](ProvidersApi.md#list_provider_configurations) | **GET** /tf/provider/{provider-name}/configurations | 
[**list_providers**](ProvidersApi.md#list_providers) | **GET** /tf/providers/ | 
[**update_provider**](ProvidersApi.md#update_provider) | **PUT** /tf/provider/{name} | 


# **create_provider**
> ResourceTfProvider create_provider(terraform_provider=terraform_provider)



Upload a Terraform provider

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
terraform_provider = swagger_client.ResourceTfProvider() # ResourceTfProvider | A terraform module (optional)

try:
    api_response = api_instance.create_provider(terraform_provider=terraform_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->create_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terraform_provider** | [**ResourceTfProvider**](ResourceTfProvider.md)| A terraform module | [optional] 

### Return type

[**ResourceTfProvider**](ResourceTfProvider.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_provider_configuration**
> ResourceTfProviderConfiguration create_provider_configuration(provider_name, provider_configuration)



Create a Terraform Provider Configuration

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
provider_name = 'provider_name_example' # str | Terraform Provider Name
provider_configuration = swagger_client.ResourceTfProviderConfiguration() # ResourceTfProviderConfiguration | A terraform provider configuration

try:
    api_response = api_instance.create_provider_configuration(provider_name, provider_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->create_provider_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**| Terraform Provider Name | 
 **provider_configuration** | [**ResourceTfProviderConfiguration**](ResourceTfProviderConfiguration.md)| A terraform provider configuration | 

### Return type

[**ResourceTfProviderConfiguration**](ResourceTfProviderConfiguration.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provider**
> delete_provider(name)



Delete a terraform provider

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Unique identifier for this provider

try:
    api_instance.delete_provider(name)
except ApiException as e:
    print("Exception when calling ProvidersApi->delete_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Unique identifier for this provider | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provider_configuration**
> delete_provider_configuration(provider_name, id)



Delete a terraform provider configuration

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
provider_name = 'provider_name_example' # str | Terraform Provider ID
id = 'id_example' # str | Configuration for a Terraform Provider

try:
    api_instance.delete_provider_configuration(provider_name, id)
except ApiException as e:
    print("Exception when calling ProvidersApi->delete_provider_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**| Terraform Provider ID | 
 **id** | **str**| Configuration for a Terraform Provider | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider**
> ResourceTfProvider get_provider(name)



Get Terraform Provider

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Terraform Provider Name

try:
    api_response = api_instance.get_provider(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->get_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Terraform Provider Name | 

### Return type

[**ResourceTfProvider**](ResourceTfProvider.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_configuration**
> ResourceTfProviderConfiguration get_provider_configuration(provider_name, id)



Get Configuration for Provider

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
provider_name = 'provider_name_example' # str | Terraform Provider ID
id = 'id_example' # str | Configuration for a Terraform Provider

try:
    api_response = api_instance.get_provider_configuration(provider_name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->get_provider_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**| Terraform Provider ID | 
 **id** | **str**| Configuration for a Terraform Provider | 

### Return type

[**ResourceTfProviderConfiguration**](ResourceTfProviderConfiguration.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_provider_configurations**
> ResponseListTfProviderConfiguration list_provider_configurations(provider_name)



List Configurations for s Terraform Provider

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
provider_name = 'provider_name_example' # str | Terraform Provider Name

try:
    api_response = api_instance.list_provider_configurations(provider_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->list_provider_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**| Terraform Provider Name | 

### Return type

[**ResponseListTfProviderConfiguration**](ResponseListTfProviderConfiguration.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> ResponseListTfProviders list_providers()



List Terraform Providers

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_providers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->list_providers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseListTfProviders**](ResponseListTfProviders.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provider**
> ResourceTfProvider update_provider(name, terraform_provider=terraform_provider)



Update a Terraform provider

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Terraform Provider ID
terraform_provider = swagger_client.ResourceTfProvider() # ResourceTfProvider | A terraform provider (optional)

try:
    api_response = api_instance.update_provider(name, terraform_provider=terraform_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->update_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Terraform Provider ID | 
 **terraform_provider** | [**ResourceTfProvider**](ResourceTfProvider.md)| A terraform provider | [optional] 

### Return type

[**ResourceTfProvider**](ResourceTfProvider.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.lunaform.v1+json
 - **Accept**: application/vnd.lunaform.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

