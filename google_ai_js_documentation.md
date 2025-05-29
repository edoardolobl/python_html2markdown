# Comprehensive Documentation for https://googleapis.github.io/js-genai/

Generated on: 2025-05-28 21:41:55

---

## DeleteCachedContentParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.DeleteCachedContentParameters.html

# Interface DeleteCachedContentParameters

Parameters for caches.delete method.

- Defined in types.ts:3465

Index

### Properties

Properties

### Optionalconfig

Optional parameters for the request.

- Defined in types.ts:3471

### name

The server-generated resource name of the cached content.

- Defined in types.ts:3468

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## DeleteFileParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.DeleteFileParameters.html

# Interface DeleteFileParameters

Generates the parameters for the get method.

- Defined in types.ts:3716

Index

### Properties

Properties

### Optionalconfig

Used to override the default configuration.

- Defined in types.ts:3720

### name

The name identifier for the file to be deleted.

- Defined in types.ts:3718

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## DeleteModelParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.DeleteModelParameters.html

# Interface DeleteModelParameters

Parameters for deleting a tuned model.

- Defined in types.ts:2718

Index

### Properties

Properties

### Optionalconfig

Optional parameters for the request.

- Defined in types.ts:2721

### model

- Defined in types.ts:2719

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Files | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/files.Files.html#download

# Class Files

#### Hierarchy

- BaseModule
    - Files

- Defined in files.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Files ( apiClient : ApiClient ) : Files Parameters Returns Files Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Files

Overrides BaseModule.constructor

- Defined in files.ts:17

Methods

### delete

- delete ( params : DeleteFileParameters ) : Promise &lt; DeleteFileResponse &gt; Deletes a remotely stored file. Parameters Returns Promise &lt; DeleteFileResponse &gt; The DeleteFileResponse, the response for the delete method. Example The following code deletes an example file named "files/mehozpxf877d". await ai . files . delete ({ name: file . name }); Copy
- Deletes a remotely stored file.

#### Parameters

- params: DeleteFileParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteFileResponse&gt;

The DeleteFileResponse, the response for the delete method.

#### Example

The following code deletes an example file named "files/mehozpxf877d".

```
await ai.files.delete({name: file.name});
Copy
```

- Defined in files.ts:288

### download

- download ( params : DownloadFileParameters ) : Promise &lt; void &gt; Downloads a remotely stored file asynchronously to a location specified inthe params object. This method only works on Node environment, todownload files in the browser, use a browser compliant method like an tag. Parameters Returns Promise &lt; void &gt; Example The following code downloads an example file named "files/mehozpxf877d" as"file.txt". await ai . files . download ({ file: file . name , downloadPath: 'file.txt' }); Copy
- Downloads a remotely stored file asynchronously to a location specified in
the params object. This method only works on Node environment, to
download files in the browser, use a browser compliant method like an 
tag.

#### Parameters

- params: DownloadFileParametersThe parameters for the download request.

#### Returns Promise&lt;void&gt;

#### Example

The following code downloads an example file named "files/mehozpxf877d" as
"file.txt".

```
await ai.files.download({file: file.name, downloadPath: 'file.txt'});
Copy
```

- Defined in files.ts:124

### get

- get ( params : GetFileParameters ) : Promise &lt; File &gt; Retrieves the file information from the service. Parameters Returns Promise &lt; File &gt; The Promise that resolves to the types.File object requested. Example const config : GetFileParameters = { name: fileName , }; file = await ai . files . get ( config ); console . log ( file . name ); Copy
- Retrieves the file information from the service.

#### Parameters

- params: GetFileParametersThe parameters for the get request

#### Returns Promise&lt;File&gt;

The Promise that resolves to the types.File object requested.

#### Example

```
const config: GetFileParameters = {
  name: fileName,
};
file = await ai.files.get(config);
console.log(file.name);
Copy
```

- Defined in files.ts:235

### list

- list ( params ?: ListFilesParameters ) : Promise &lt; Pager &lt; File &gt; &gt; Lists all current project files from the service. Parameters Returns Promise &lt; Pager &lt; File &gt; &gt; The paginated results of the list of files Example The following code prints the names of all files from the service, thesize of each page is 10. const listResponse = await ai . files . list ({ config: { 'pageSize' : 10 }}); for await ( const file of listResponse ) { console . log ( file . name ); } Copy
- Lists all current project files from the service.

#### Parameters

- params: ListFilesParameters = {}The parameters for the list request

#### Returns Promise&lt;Pager&lt;File&gt;&gt;

The paginated results of the list of files

#### Example

The following code prints the names of all files from the service, the
size of each page is 10.

```
const listResponse = await ai.files.list({config: {'pageSize': 10}});
for await (const file of listResponse) {
  console.log(file.name);
}
Copy
```

- Defined in files.ts:38

### upload

- upload ( params : UploadFileParameters ) : Promise &lt; File &gt; Uploads a file asynchronously to the Gemini API.This method is not available in Vertex AI.Supported upload sources: Parameters Returns Promise &lt; File &gt; A promise that resolves to a types.File object. Remarks The mimeType can be specified in the config parameter. If omitted: This section can contain multiple paragraphs and code examples. See types.UploadFileParameters#config for the optionalconfig in the parameters. Throws An error if called on a Vertex AI client. Throws An error if the mimeType is not provided and can not be inferred,the mimeType can be provided in the params.config parameter. Throws An error occurs if a suitable upload location cannot be established. Example The following code uploads a file to Gemini API. const file = await ai . files . upload ({ file: 'file.txt' , config: { mimeType: 'text/plain' , }}); console . log ( file . name ); Copy
- Uploads a file asynchronously to the Gemini API.
This method is not available in Vertex AI.
Supported upload sources:
    - Node.js: File path (string) or Blob object.
    - Browser: Blob object (e.g., File).

#### Parameters

- params: UploadFileParametersOptional parameters specified in the
types.UploadFileParameters interface.

#### Returns Promise&lt;File&gt;

A promise that resolves to a types.File object.

#### Remarks

The mimeType can be specified in the config parameter. If omitted:

- For file path (string) inputs, the mimeType will be inferred from the
file extension.
- For Blob object inputs, the mimeType will be set to the Blob's type
property.
Somex eamples for file extension to mimeType mapping:
.txt -&gt; text/plain
.json -&gt; application/json
.jpg  -&gt; image/jpeg
.png -&gt; image/png
.mp3 -&gt; audio/mpeg
.mp4 -&gt; video/mp4

This section can contain multiple paragraphs and code examples.

#### See

types.UploadFileParameters#config for the optional
config in the parameters.

#### Throws

An error if called on a Vertex AI client.

#### Throws

An error if the mimeType is not provided and can not be inferred,
the mimeType can be provided in the params.config parameter.

#### Throws

An error occurs if a suitable upload location cannot be established.

#### Example

The following code uploads a file to Gemini API.

```
const file = await ai.files.upload({file: 'file.txt', config: {
  mimeType: 'text/plain',
}});
console.log(file.name);
Copy
```

- Defined in files.ts:92

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## LiveConnectParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.LiveConnectParameters.html

# Interface LiveConnectParameters

Parameters for connecting to the live API.

- Defined in types.ts:4578

Index

### Properties

Properties

### callbacks

callbacks

- Defined in types.ts:4583

### Optionalconfig

Optional configuration parameters for the request.

- Defined in types.ts:4586

### model

ID of the model to use. For a list of models, see Google models &lt;https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models&gt;\_.

- Defined in types.ts:4581

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#editimage

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## DownloadFileParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.DownloadFileParameters.html

# Interface DownloadFileParameters

Parameters used to download a file.

- Defined in types.ts:3854

Index

### Properties

Properties

### Optionalconfig

Configuration to for the download operation.

- Defined in types.ts:3860

### downloadPath

Location where the file should be downloaded to.

- Defined in types.ts:3858

### file

The file to download. It can be a file name, a file object or a generated video.

- Defined in types.ts:3856

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## DeleteModelResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.DeleteModelResponse.html

# Class DeleteModelResponse

- Defined in types.ts:2724

Index

### Constructors

Constructors

### constructor

- new DeleteModelResponse(): DeleteModelResponseReturns DeleteModelResponse

Settings

On This Page

Constructors

- Loading...

Generated using TypeDoc

---

## UpscaleImageParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.UpscaleImageParameters.html

# Interface UpscaleImageParameters

User-facing config UpscaleImageParameters.

- Defined in types.ts:3890

Index

### Properties

Properties

### Optionalconfig

Configuration for upscaling.

- Defined in types.ts:3898

### image

The input image to upscale.

- Defined in types.ts:3894

### model

The model to use.

- Defined in types.ts:3892

### upscaleFactor

The factor to upscale the image (x2 or x4).

- Defined in types.ts:3896

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## chats | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/chats.html

# Module chats

Classes

Settings

On This Page

Classes

- Loading...

Generated using TypeDoc

---

## CountTokensParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.CountTokensParameters.html

# Interface CountTokensParameters

Parameters for counting tokens.

- Defined in types.ts:2803

Index

### Properties

Properties

### Optionalconfig

Configuration for counting tokens.

- Defined in types.ts:2810

### contents

Input content.

- Defined in types.ts:2808

### model

ID of the model to use. For a list of models, see Google models &lt;https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models&gt;\_.

- Defined in types.ts:2806

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## GenerateImagesResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.GenerateImagesResponse.html

# Class GenerateImagesResponse

The output images response.

- Defined in types.ts:2452

Index

### Constructors

### Properties

Constructors

### constructor

- new GenerateImagesResponse(): GenerateImagesResponseReturns GenerateImagesResponse

Properties

### OptionalgeneratedImages

List of generated images.

- Defined in types.ts:2455

### OptionalpositivePromptSafetyAttributes

Safety attributes of the positive prompt. Only populated if
include\_safety\_attributes is set to True.

- Defined in types.ts:2459

Settings

On This Page

Constructors

Properties

- Loading...

Generated using TypeDoc

---

## DeleteCachedContentResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.DeleteCachedContentResponse.html

# Class DeleteCachedContentResponse

Empty response for caches.delete method.

- Defined in types.ts:3475

Index

### Constructors

Constructors

### constructor

- new DeleteCachedContentResponse(): DeleteCachedContentResponseReturns DeleteCachedContentResponse

Settings

On This Page

Constructors

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#counttokens

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## GenerateContentResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.GenerateContentResponse.html

# Class GenerateContentResponse

Response message for PredictionService.GenerateContent.

- Defined in types.ts:1943

Index

### Constructors

### Properties

### Accessors

Constructors

### constructor

- new GenerateContentResponse(): GenerateContentResponseReturns GenerateContentResponse

Properties

### OptionalautomaticFunctionCallingHistory

The history of automatic function calling.

- Defined in types.ts:1955

### Optionalcandidates

Response variations returned by the model.

- Defined in types.ts:1946

### OptionalcreateTime

Timestamp when the request is made to the server.

- Defined in types.ts:1949

### OptionalmodelVersion

Output only. The model version used to generate the response.

- Defined in types.ts:1957

### OptionalpromptFeedback

Output only. Content filter results for a prompt sent in the request. Note: Sent only in the first stream chunk. Only happens when no candidates were generated due to content violations.

- Defined in types.ts:1959

### OptionalresponseId

Identifier for each response.

- Defined in types.ts:1952

### OptionalusageMetadata

Usage metadata about the response(s).

- Defined in types.ts:1961

Accessors

### codeExecutionResult

- get codeExecutionResult () : undefined | string Returns the first code execution result from the first candidate in the response. Returns undefined | string Remarks If there are multiple candidates in the response, the code execution result fromthe first one will be returned.If there are no code execution result in the response, undefined will be returned. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.' config : { tools: [{ codeExecution: {}}], }, }); console . debug ( response . codeExecutionResult ); Copy
- Returns the first code execution result from the first candidate in the response.

#### Returns undefined | string

#### Remarks

If there are multiple candidates in the response, the code execution result from
the first one will be returned.
If there are no code execution result in the response, undefined will be returned.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents:
    'What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.'
  config: {
    tools: [{codeExecution: {}}],
  },
});

console.debug(response.codeExecutionResult);
Copy
```

- Defined in types.ts:2198

### data

- get data () : undefined | string Returns the concatenation of all inline data parts from the first candidatein the response. Returns undefined | string Remarks If there are multiple candidates in the response, the inline data from thefirst one will be returned. If there are non-inline data parts in theresponse, the concatenation of all inline data parts will be returned, anda warning will be logged.
- Returns the concatenation of all inline data parts from the first candidate
in the response.

#### Returns undefined | string

#### Remarks

If there are multiple candidates in the response, the inline data from the
first one will be returned. If there are non-inline data parts in the
response, the concatenation of all inline data parts will be returned, and
a warning will be logged.

- Defined in types.ts:2033

### executableCode

- get executableCode () : undefined | string Returns the first executable code from the first candidate in the response. Returns undefined | string Remarks If there are multiple candidates in the response, the executable code fromthe first one will be returned.If there are no executable code in the response, undefined will bereturned. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.' config : { tools: [{ codeExecution: {}}], }, }); console . debug ( response . executableCode ); Copy
- Returns the first executable code from the first candidate in the response.

#### Returns undefined | string

#### Remarks

If there are multiple candidates in the response, the executable code from
the first one will be returned.
If there are no executable code in the response, undefined will be
returned.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents:
    'What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.'
  config: {
    tools: [{codeExecution: {}}],
  },
});

console.debug(response.executableCode);
Copy
```

- Defined in types.ts:2154

### functionCalls

- get functionCalls () : undefined | FunctionCall [] Returns the function calls from the first candidate in the response. Returns undefined | FunctionCall [] Remarks If there are multiple candidates in the response, the function calls fromthe first one will be returned.If there are no function calls in the response, undefined will be returned. Example const controlLightFunctionDeclaration : FunctionDeclaration = { name: 'controlLight' , parameters: { type: Type . OBJECT , description: 'Set the brightness and color temperature of a room light.' , properties: { brightness: { type: Type . NUMBER , description: 'Light level from 0 to 100. Zero is off and 100 is full brightness.' , }, colorTemperature: { type: Type . STRING , description: 'Color temperature of the light fixture which can be `daylight`, `cool` or `warm`.' , }, }, required: [ 'brightness' , 'colorTemperature' ], }; const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'Dim the lights so the room feels cozy and warm.' , config: { tools: [{ functionDeclarations: [ controlLightFunctionDeclaration ]}], toolConfig: { functionCallingConfig: { mode: FunctionCallingConfigMode . ANY , allowedFunctionNames: [ 'controlLight' ], }, }, }, }); console . debug ( JSON . stringify ( response . functionCalls )); Copy
- Returns the function calls from the first candidate in the response.

#### Returns undefined | FunctionCall[]

#### Remarks

If there are multiple candidates in the response, the function calls from
the first one will be returned.
If there are no function calls in the response, undefined will be returned.

#### Example

```
const controlLightFunctionDeclaration: FunctionDeclaration = {
  name: 'controlLight',
  parameters: {
  type: Type.OBJECT,
  description: 'Set the brightness and color temperature of a room light.',
  properties: {
    brightness: {
      type: Type.NUMBER,
      description:
        'Light level from 0 to 100. Zero is off and 100 is full brightness.',
    },
    colorTemperature: {
      type: Type.STRING,
      description:
        'Color temperature of the light fixture which can be `daylight`, `cool` or `warm`.',
    },
  },
  required: ['brightness', 'colorTemperature'],
 };
 const response = await ai.models.generateContent({
    model: 'gemini-2.0-flash',
    contents: 'Dim the lights so the room feels cozy and warm.',
    config: {
      tools: [{functionDeclarations: [controlLightFunctionDeclaration]}],
      toolConfig: {
        functionCallingConfig: {
          mode: FunctionCallingConfigMode.ANY,
          allowedFunctionNames: ['controlLight'],
        },
      },
    },
  });
 console.debug(JSON.stringify(response.functionCalls));
Copy
```

- Defined in types.ts:2110

### text

- get text () : undefined | string Returns the concatenation of all text parts from the first candidate in the response. Returns undefined | string Remarks If there are multiple candidates in the response, the text from the firstone will be returned.If there are non-text parts in the response, the concatenation of all textparts will be returned, and a warning will be logged.If there are thought parts in the response, the concatenation of all textparts excluding the thought parts will be returned. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'Why is the sky blue?' , }); console . debug ( response . text ); Copy
- Returns the concatenation of all text parts from the first candidate in the response.

#### Returns undefined | string

#### Remarks

If there are multiple candidates in the response, the text from the first
one will be returned.
If there are non-text parts in the response, the concatenation of all text
parts will be returned, and a warning will be logged.
If there are thought parts in the response, the concatenation of all text
parts excluding the thought parts will be returned.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents:
    'Why is the sky blue?',
});

console.debug(response.text);
Copy
```

- Defined in types.ts:1984

Settings

On This Page

Constructors

Properties

Accessors

- Loading...

Generated using TypeDoc

---

## Files | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/files.Files.html

# Class Files

#### Hierarchy

- BaseModule
    - Files

- Defined in files.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Files ( apiClient : ApiClient ) : Files Parameters Returns Files Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Files

Overrides BaseModule.constructor

- Defined in files.ts:17

Methods

### delete

- delete ( params : DeleteFileParameters ) : Promise &lt; DeleteFileResponse &gt; Deletes a remotely stored file. Parameters Returns Promise &lt; DeleteFileResponse &gt; The DeleteFileResponse, the response for the delete method. Example The following code deletes an example file named "files/mehozpxf877d". await ai . files . delete ({ name: file . name }); Copy
- Deletes a remotely stored file.

#### Parameters

- params: DeleteFileParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteFileResponse&gt;

The DeleteFileResponse, the response for the delete method.

#### Example

The following code deletes an example file named "files/mehozpxf877d".

```
await ai.files.delete({name: file.name});
Copy
```

- Defined in files.ts:288

### download

- download ( params : DownloadFileParameters ) : Promise &lt; void &gt; Downloads a remotely stored file asynchronously to a location specified inthe params object. This method only works on Node environment, todownload files in the browser, use a browser compliant method like an tag. Parameters Returns Promise &lt; void &gt; Example The following code downloads an example file named "files/mehozpxf877d" as"file.txt". await ai . files . download ({ file: file . name , downloadPath: 'file.txt' }); Copy
- Downloads a remotely stored file asynchronously to a location specified in
the params object. This method only works on Node environment, to
download files in the browser, use a browser compliant method like an 
tag.

#### Parameters

- params: DownloadFileParametersThe parameters for the download request.

#### Returns Promise&lt;void&gt;

#### Example

The following code downloads an example file named "files/mehozpxf877d" as
"file.txt".

```
await ai.files.download({file: file.name, downloadPath: 'file.txt'});
Copy
```

- Defined in files.ts:124

### get

- get ( params : GetFileParameters ) : Promise &lt; File &gt; Retrieves the file information from the service. Parameters Returns Promise &lt; File &gt; The Promise that resolves to the types.File object requested. Example const config : GetFileParameters = { name: fileName , }; file = await ai . files . get ( config ); console . log ( file . name ); Copy
- Retrieves the file information from the service.

#### Parameters

- params: GetFileParametersThe parameters for the get request

#### Returns Promise&lt;File&gt;

The Promise that resolves to the types.File object requested.

#### Example

```
const config: GetFileParameters = {
  name: fileName,
};
file = await ai.files.get(config);
console.log(file.name);
Copy
```

- Defined in files.ts:235

### list

- list ( params ?: ListFilesParameters ) : Promise &lt; Pager &lt; File &gt; &gt; Lists all current project files from the service. Parameters Returns Promise &lt; Pager &lt; File &gt; &gt; The paginated results of the list of files Example The following code prints the names of all files from the service, thesize of each page is 10. const listResponse = await ai . files . list ({ config: { 'pageSize' : 10 }}); for await ( const file of listResponse ) { console . log ( file . name ); } Copy
- Lists all current project files from the service.

#### Parameters

- params: ListFilesParameters = {}The parameters for the list request

#### Returns Promise&lt;Pager&lt;File&gt;&gt;

The paginated results of the list of files

#### Example

The following code prints the names of all files from the service, the
size of each page is 10.

```
const listResponse = await ai.files.list({config: {'pageSize': 10}});
for await (const file of listResponse) {
  console.log(file.name);
}
Copy
```

- Defined in files.ts:38

### upload

- upload ( params : UploadFileParameters ) : Promise &lt; File &gt; Uploads a file asynchronously to the Gemini API.This method is not available in Vertex AI.Supported upload sources: Parameters Returns Promise &lt; File &gt; A promise that resolves to a types.File object. Remarks The mimeType can be specified in the config parameter. If omitted: This section can contain multiple paragraphs and code examples. See types.UploadFileParameters#config for the optionalconfig in the parameters. Throws An error if called on a Vertex AI client. Throws An error if the mimeType is not provided and can not be inferred,the mimeType can be provided in the params.config parameter. Throws An error occurs if a suitable upload location cannot be established. Example The following code uploads a file to Gemini API. const file = await ai . files . upload ({ file: 'file.txt' , config: { mimeType: 'text/plain' , }}); console . log ( file . name ); Copy
- Uploads a file asynchronously to the Gemini API.
This method is not available in Vertex AI.
Supported upload sources:
    - Node.js: File path (string) or Blob object.
    - Browser: Blob object (e.g., File).

#### Parameters

- params: UploadFileParametersOptional parameters specified in the
types.UploadFileParameters interface.

#### Returns Promise&lt;File&gt;

A promise that resolves to a types.File object.

#### Remarks

The mimeType can be specified in the config parameter. If omitted:

- For file path (string) inputs, the mimeType will be inferred from the
file extension.
- For Blob object inputs, the mimeType will be set to the Blob's type
property.
Somex eamples for file extension to mimeType mapping:
.txt -&gt; text/plain
.json -&gt; application/json
.jpg  -&gt; image/jpeg
.png -&gt; image/png
.mp3 -&gt; audio/mpeg
.mp4 -&gt; video/mp4

This section can contain multiple paragraphs and code examples.

#### See

types.UploadFileParameters#config for the optional
config in the parameters.

#### Throws

An error if called on a Vertex AI client.

#### Throws

An error if the mimeType is not provided and can not be inferred,
the mimeType can be provided in the params.config parameter.

#### Throws

An error occurs if a suitable upload location cannot be established.

#### Example

The following code uploads a file to Gemini API.

```
const file = await ai.files.upload({file: 'file.txt', config: {
  mimeType: 'text/plain',
}});
console.log(file.name);
Copy
```

- Defined in files.ts:92

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Chats | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/chats.Chats.html#constructor

# Class Chats

A utility class to create a chat session.

- Defined in chats.ts:104

Index

### Constructors

### Methods

Constructors

### constructor

- new Chats ( modelsModule : Models , apiClient : ApiClient ) : Chats Parameters Returns Chats

#### Parameters

- modelsModule: Models
- apiClient: ApiClient

#### Returns Chats

- Defined in chats.ts:108

Methods

### create

- create ( params : CreateChatParameters ) : Chat Creates a new chat session. Parameters Returns Chat A new chat session. Remarks The config in the params will be used for all requests within the chatsession unless overridden by a per-request config in See types.SendMessageParameters#config . Example const chat = ai . chats . create ({ model: 'gemini-2.0-flash' config : { temperature: 0.5 , maxOutputTokens: 1024 , } }); Copy
- Creates a new chat session.

#### Parameters

- params: CreateChatParametersParameters for creating a chat session.

#### Returns Chat

A new chat session.

#### Remarks

The config in the params will be used for all requests within the chat
session unless overridden by a per-request config in

#### See

types.SendMessageParameters#config.

#### Example

```
const chat = ai.chats.create({
  model: 'gemini-2.0-flash'
  config: {
    temperature: 0.5,
    maxOutputTokens: 1024,
  }
});
Copy
```

- Defined in chats.ts:135

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## types | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/types.html

# Module types

Enumerations

Classes

Interfaces

Type Aliases

Functions

Settings

On This Page

Enumerations

Classes

Interfaces

Type Aliases

Functions

- Loading...

Generated using TypeDoc

---

## GenerateVideosOperation | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.GenerateVideosOperation.html

# Interface GenerateVideosOperation

A video generation operation.

- Defined in types.ts:2938

Index

### Properties

Properties

### Optionaldone

If the value is false, it means the operation is still in progress. If true, the operation is completed, and either error or response is available.

- Defined in types.ts:2944

### Optionalerror

The error result of the operation in case of failure or cancellation.

- Defined in types.ts:2946

### Optionalmetadata

Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata.  Any method that returns a long-running operation should document the metadata type, if any.

- Defined in types.ts:2942

### Optionalname

The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the name should be a resource name ending with operations/{unique\_id}.

- Defined in types.ts:2940

### Optionalresponse

The generated videos.

- Defined in types.ts:2948

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#generatevideos

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## CountTokensResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.CountTokensResponse.html

# Class CountTokensResponse

Response for counting tokens.

- Defined in types.ts:2814

Index

### Constructors

### Properties

Constructors

### constructor

- new CountTokensResponse(): CountTokensResponseReturns CountTokensResponse

Properties

### OptionalcachedContentTokenCount

Number of tokens in the cached part of the prompt (the cached content).

- Defined in types.ts:2818

### OptionaltotalTokens

Total number of tokens.

- Defined in types.ts:2816

Settings

On This Page

Constructors

Properties

- Loading...

Generated using TypeDoc

---

## ListModelsParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.ListModelsParameters.html

# Interface ListModelsParameters

- Defined in types.ts:2673

Index

### Properties

Properties

### Optionalconfig

- Defined in types.ts:2674

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## DeleteFileResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.DeleteFileResponse.html

# Class DeleteFileResponse

Response for the delete file method.

- Defined in types.ts:3724

Index

### Constructors

Constructors

### constructor

- new DeleteFileResponse(): DeleteFileResponseReturns DeleteFileResponse

Settings

On This Page

Constructors

- Loading...

Generated using TypeDoc

---

## UpdateModelParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.UpdateModelParameters.html

# Interface UpdateModelParameters

Configuration for updating a tuned model.

- Defined in types.ts:2699

Index

### Properties

Properties

### Optionalconfig

- Defined in types.ts:2701

### model

- Defined in types.ts:2700

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#get

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Files | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/files.Files.html#upload

# Class Files

#### Hierarchy

- BaseModule
    - Files

- Defined in files.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Files ( apiClient : ApiClient ) : Files Parameters Returns Files Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Files

Overrides BaseModule.constructor

- Defined in files.ts:17

Methods

### delete

- delete ( params : DeleteFileParameters ) : Promise &lt; DeleteFileResponse &gt; Deletes a remotely stored file. Parameters Returns Promise &lt; DeleteFileResponse &gt; The DeleteFileResponse, the response for the delete method. Example The following code deletes an example file named "files/mehozpxf877d". await ai . files . delete ({ name: file . name }); Copy
- Deletes a remotely stored file.

#### Parameters

- params: DeleteFileParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteFileResponse&gt;

The DeleteFileResponse, the response for the delete method.

#### Example

The following code deletes an example file named "files/mehozpxf877d".

```
await ai.files.delete({name: file.name});
Copy
```

- Defined in files.ts:288

### download

- download ( params : DownloadFileParameters ) : Promise &lt; void &gt; Downloads a remotely stored file asynchronously to a location specified inthe params object. This method only works on Node environment, todownload files in the browser, use a browser compliant method like an tag. Parameters Returns Promise &lt; void &gt; Example The following code downloads an example file named "files/mehozpxf877d" as"file.txt". await ai . files . download ({ file: file . name , downloadPath: 'file.txt' }); Copy
- Downloads a remotely stored file asynchronously to a location specified in
the params object. This method only works on Node environment, to
download files in the browser, use a browser compliant method like an 
tag.

#### Parameters

- params: DownloadFileParametersThe parameters for the download request.

#### Returns Promise&lt;void&gt;

#### Example

The following code downloads an example file named "files/mehozpxf877d" as
"file.txt".

```
await ai.files.download({file: file.name, downloadPath: 'file.txt'});
Copy
```

- Defined in files.ts:124

### get

- get ( params : GetFileParameters ) : Promise &lt; File &gt; Retrieves the file information from the service. Parameters Returns Promise &lt; File &gt; The Promise that resolves to the types.File object requested. Example const config : GetFileParameters = { name: fileName , }; file = await ai . files . get ( config ); console . log ( file . name ); Copy
- Retrieves the file information from the service.

#### Parameters

- params: GetFileParametersThe parameters for the get request

#### Returns Promise&lt;File&gt;

The Promise that resolves to the types.File object requested.

#### Example

```
const config: GetFileParameters = {
  name: fileName,
};
file = await ai.files.get(config);
console.log(file.name);
Copy
```

- Defined in files.ts:235

### list

- list ( params ?: ListFilesParameters ) : Promise &lt; Pager &lt; File &gt; &gt; Lists all current project files from the service. Parameters Returns Promise &lt; Pager &lt; File &gt; &gt; The paginated results of the list of files Example The following code prints the names of all files from the service, thesize of each page is 10. const listResponse = await ai . files . list ({ config: { 'pageSize' : 10 }}); for await ( const file of listResponse ) { console . log ( file . name ); } Copy
- Lists all current project files from the service.

#### Parameters

- params: ListFilesParameters = {}The parameters for the list request

#### Returns Promise&lt;Pager&lt;File&gt;&gt;

The paginated results of the list of files

#### Example

The following code prints the names of all files from the service, the
size of each page is 10.

```
const listResponse = await ai.files.list({config: {'pageSize': 10}});
for await (const file of listResponse) {
  console.log(file.name);
}
Copy
```

- Defined in files.ts:38

### upload

- upload ( params : UploadFileParameters ) : Promise &lt; File &gt; Uploads a file asynchronously to the Gemini API.This method is not available in Vertex AI.Supported upload sources: Parameters Returns Promise &lt; File &gt; A promise that resolves to a types.File object. Remarks The mimeType can be specified in the config parameter. If omitted: This section can contain multiple paragraphs and code examples. See types.UploadFileParameters#config for the optionalconfig in the parameters. Throws An error if called on a Vertex AI client. Throws An error if the mimeType is not provided and can not be inferred,the mimeType can be provided in the params.config parameter. Throws An error occurs if a suitable upload location cannot be established. Example The following code uploads a file to Gemini API. const file = await ai . files . upload ({ file: 'file.txt' , config: { mimeType: 'text/plain' , }}); console . log ( file . name ); Copy
- Uploads a file asynchronously to the Gemini API.
This method is not available in Vertex AI.
Supported upload sources:
    - Node.js: File path (string) or Blob object.
    - Browser: Blob object (e.g., File).

#### Parameters

- params: UploadFileParametersOptional parameters specified in the
types.UploadFileParameters interface.

#### Returns Promise&lt;File&gt;

A promise that resolves to a types.File object.

#### Remarks

The mimeType can be specified in the config parameter. If omitted:

- For file path (string) inputs, the mimeType will be inferred from the
file extension.
- For Blob object inputs, the mimeType will be set to the Blob's type
property.
Somex eamples for file extension to mimeType mapping:
.txt -&gt; text/plain
.json -&gt; application/json
.jpg  -&gt; image/jpeg
.png -&gt; image/png
.mp3 -&gt; audio/mpeg
.mp4 -&gt; video/mp4

This section can contain multiple paragraphs and code examples.

#### See

types.UploadFileParameters#config for the optional
config in the parameters.

#### Throws

An error if called on a Vertex AI client.

#### Throws

An error if the mimeType is not provided and can not be inferred,
the mimeType can be provided in the params.config parameter.

#### Throws

An error occurs if a suitable upload location cannot be established.

#### Example

The following code uploads a file to Gemini API.

```
const file = await ai.files.upload({file: 'file.txt', config: {
  mimeType: 'text/plain',
}});
console.log(file.name);
Copy
```

- Defined in files.ts:92

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Caches | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/caches.Caches.html#list

# Class Caches

#### Hierarchy

- BaseModule
    - Caches

- Defined in caches.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Caches ( apiClient : ApiClient ) : Caches Parameters Returns Caches Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Caches

Overrides BaseModule.constructor

- Defined in caches.ts:17

Methods

### create

- create ( params : CreateCachedContentParameters ) : Promise &lt; CachedContent &gt; Creates a cached contents resource. Parameters Returns Promise &lt; CachedContent &gt; The created cached content. Remarks Context caching is only supported for specific models. See GeminiDeveloper API reference and Vertex AI reference for more information. Example const contents = ...; // Initialize the content to cache. const response = await ai . caches . create ({ model: 'gemini-2.0-flash-001' , config: { 'contents' : contents , 'displayName' : 'test cache' , 'systemInstruction' : 'What is the sum of the two pdfs?' , 'ttl' : '86400s' , } }); Copy
- Creates a cached contents resource.

#### Parameters

- params: CreateCachedContentParametersThe parameters for the create request.

#### Returns Promise&lt;CachedContent&gt;

The created cached content.

#### Remarks

Context caching is only supported for specific models. See Gemini
Developer API reference
and Vertex AI reference
for more information.

#### Example

```
const contents = ...; // Initialize the content to cache.
const response = await ai.caches.create({
  model: 'gemini-2.0-flash-001',
  config: {
   'contents': contents,
   'displayName': 'test cache',
   'systemInstruction': 'What is the sum of the two pdfs?',
   'ttl': '86400s',
 }
});
Copy
```

- Defined in caches.ts:72

### delete

- delete ( params : DeleteCachedContentParameters , ) : Promise &lt; DeleteCachedContentResponse &gt; Deletes cached content. Parameters Returns Promise &lt; DeleteCachedContentResponse &gt; The empty response returned by the API. Example await ai . caches . delete ({ name: '...' }); // The server-generated resource name. Copy
- Deletes cached content.

#### Parameters

- params: DeleteCachedContentParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteCachedContentResponse&gt;

The empty response returned by the API.

#### Example

```
await ai.caches.delete({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:252

### get

- get ( params : GetCachedContentParameters ) : Promise &lt; CachedContent &gt; Gets cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The cached content. Example await ai . caches . get ({ name: '...' }); // The server-generated resource name. Copy
- Gets cached content configurations.

#### Parameters

- params: GetCachedContentParametersThe parameters for the get request.

#### Returns Promise&lt;CachedContent&gt;

The cached content.

#### Example

```
await ai.caches.get({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:162

### list

- list ( params ?: ListCachedContentsParameters ) : Promise &lt; Pager &lt; CachedContent &gt; &gt; Lists cached content configurations. Parameters Returns Promise &lt; Pager &lt; CachedContent &gt; &gt; The paginated results of the list of cached contents. Example const cachedContents = await ai . caches . list ({ config: { 'pageSize' : 2 }}); for ( const cachedContent of cachedContents ) { console . log ( cachedContent ); } Copy
- Lists cached content configurations.

#### Parameters

- params: ListCachedContentsParameters = {}The parameters for the list request.

#### Returns Promise&lt;Pager&lt;CachedContent&gt;&gt;

The paginated results of the list of cached contents.

#### Example

```
const cachedContents = await ai.caches.list({config: {'pageSize': 2}});
for (const cachedContent of cachedContents) {
  console.log(cachedContent);
}
Copy
```

- Defined in caches.ts:35

### update

- update ( params : UpdateCachedContentParameters ) : Promise &lt; CachedContent &gt; Updates cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The updated cached content. Example const response = await ai . caches . update ({ name: '...' , // The server-generated resource name. config: { 'ttl' : '7600s' } }); Copy
- Updates cached content configurations.

#### Parameters

- params: UpdateCachedContentParametersThe parameters for the update request.

#### Returns Promise&lt;CachedContent&gt;

The updated cached content.

#### Example

```
const response = await ai.caches.update({
  name: '...',  // The server-generated resource name.
  config: {'ttl': '7600s'}
});
Copy
```

- Defined in caches.ts:341

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## ListCachedContentsParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.ListCachedContentsParameters.html

# Interface ListCachedContentsParameters

Parameters for caches.list method.

- Defined in types.ts:3519

Index

### Properties

Properties

### Optionalconfig

Configuration that contains optional parameters.

- Defined in types.ts:3522

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## ComputeTokensResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.ComputeTokensResponse.html

# Class ComputeTokensResponse

Response for computing tokens.

- Defined in types.ts:2857

Index

### Constructors

### Properties

Constructors

### constructor

- new ComputeTokensResponse(): ComputeTokensResponseReturns ComputeTokensResponse

Properties

### OptionaltokensInfo

Lists of tokens info from the input. A ComputeTokensRequest could have multiple instances with a prompt in each instance. We also need to return lists of tokens info for the request with multiple instances.

- Defined in types.ts:2859

Settings

On This Page

Constructors

Properties

- Loading...

Generated using TypeDoc

---

## Live | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/live.Live.html#music

# Class LiveExperimental

Live class encapsulates the configuration for live interaction with the
Generative Language API. It embeds ApiClient for general API settings.

- Defined in live.ts:71

Index

### Constructors

### Properties

### Methods

Constructors

### constructor

- new Live ( apiClient : ApiClient , auth : Auth , webSocketFactory : WebSocketFactory , ) : Live Experimental Parameters Returns Live
- ```
Experimental
```

#### Parameters

- apiClient: ApiClient
- auth: Auth
- webSocketFactory: WebSocketFactory

#### Returns Live

- Defined in live.ts:74

Properties

### Readonly Experimentalmusic

- Defined in live.ts:72

Methods

### connect

- connect ( params : LiveConnectParameters ) : Promise &lt; Session &gt; Experimental Establishes a connection to the specified model with the givenconfiguration and returns a Session object representing that connection. Built-in MCP support is an experimental feature, may change infuture versions. Parameters Returns Promise &lt; Session &gt; A live session. Remarks Example let model : string ; if ( GOOGLE\_GENAI\_USE\_VERTEXAI ) { model = 'gemini-2.0-flash-live-preview-04-09' ; } else { model = 'gemini-2.0-flash-live-001' ; } const session = await ai . live . connect ({ model: model , config: { responseModalities: [ Modality . AUDIO ], }, callbacks: { onopen : () =&gt; { console . log ( 'Connected to the socket.' ); }, onmessage : ( e : MessageEvent ) =&gt; { console . log ( 'Received message from the server: %s \n ' , debug ( e . data )); }, onerror : ( e : ErrorEvent ) =&gt; { console . log ( 'Error occurred: %s \n ' , debug ( e . error )); }, onclose : ( e : CloseEvent ) =&gt; { console . log ( 'Connection closed.' ); }, }, }); Copy
- ```
Experimental
```
- Establishes a connection to the specified model with the given
configuration and returns a Session object representing that connection.
- Built-in MCP support is an experimental feature, may change in
future versions.

#### Parameters

- params: LiveConnectParametersThe parameters for establishing a connection to the model.

#### Returns Promise&lt;Session&gt;

A live session.

#### Remarks

#### Example

```
let model: string;
if (GOOGLE_GENAI_USE_VERTEXAI) {
  model = 'gemini-2.0-flash-live-preview-04-09';
} else {
  model = 'gemini-2.0-flash-live-001';
}
const session = await ai.live.connect({
  model: model,
  config: {
    responseModalities: [Modality.AUDIO],
  },
  callbacks: {
    onopen: () => {
      console.log('Connected to the socket.');
    },
    onmessage: (e: MessageEvent) => {
      console.log('Received message from the server: %s\n', debug(e.data));
    },
    onerror: (e: ErrorEvent) => {
      console.log('Error occurred: %s\n', debug(e.error));
    },
    onclose: (e: CloseEvent) => {
      console.log('Connection closed.');
    },
  },
});
Copy
```

- Defined in live.ts:128

Settings

On This Page

Constructors

Properties

Methods

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#list

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## caches | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/caches.html

# Module caches

Classes

Settings

On This Page

Classes

- Loading...

Generated using TypeDoc

---

## Live | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/live.Live.html

# Class LiveExperimental

Live class encapsulates the configuration for live interaction with the
Generative Language API. It embeds ApiClient for general API settings.

- Defined in live.ts:71

Index

### Constructors

### Properties

### Methods

Constructors

### constructor

- new Live ( apiClient : ApiClient , auth : Auth , webSocketFactory : WebSocketFactory , ) : Live Experimental Parameters Returns Live
- ```
Experimental
```

#### Parameters

- apiClient: ApiClient
- auth: Auth
- webSocketFactory: WebSocketFactory

#### Returns Live

- Defined in live.ts:74

Properties

### Readonly Experimentalmusic

- Defined in live.ts:72

Methods

### connect

- connect ( params : LiveConnectParameters ) : Promise &lt; Session &gt; Experimental Establishes a connection to the specified model with the givenconfiguration and returns a Session object representing that connection. Built-in MCP support is an experimental feature, may change infuture versions. Parameters Returns Promise &lt; Session &gt; A live session. Remarks Example let model : string ; if ( GOOGLE\_GENAI\_USE\_VERTEXAI ) { model = 'gemini-2.0-flash-live-preview-04-09' ; } else { model = 'gemini-2.0-flash-live-001' ; } const session = await ai . live . connect ({ model: model , config: { responseModalities: [ Modality . AUDIO ], }, callbacks: { onopen : () =&gt; { console . log ( 'Connected to the socket.' ); }, onmessage : ( e : MessageEvent ) =&gt; { console . log ( 'Received message from the server: %s \n ' , debug ( e . data )); }, onerror : ( e : ErrorEvent ) =&gt; { console . log ( 'Error occurred: %s \n ' , debug ( e . error )); }, onclose : ( e : CloseEvent ) =&gt; { console . log ( 'Connection closed.' ); }, }, }); Copy
- ```
Experimental
```
- Establishes a connection to the specified model with the given
configuration and returns a Session object representing that connection.
- Built-in MCP support is an experimental feature, may change in
future versions.

#### Parameters

- params: LiveConnectParametersThe parameters for establishing a connection to the model.

#### Returns Promise&lt;Session&gt;

A live session.

#### Remarks

#### Example

```
let model: string;
if (GOOGLE_GENAI_USE_VERTEXAI) {
  model = 'gemini-2.0-flash-live-preview-04-09';
} else {
  model = 'gemini-2.0-flash-live-001';
}
const session = await ai.live.connect({
  model: model,
  config: {
    responseModalities: [Modality.AUDIO],
  },
  callbacks: {
    onopen: () => {
      console.log('Connected to the socket.');
    },
    onmessage: (e: MessageEvent) => {
      console.log('Received message from the server: %s\n', debug(e.data));
    },
    onerror: (e: ErrorEvent) => {
      console.log('Error occurred: %s\n', debug(e.error));
    },
    onclose: (e: CloseEvent) => {
      console.log('Connection closed.');
    },
  },
});
Copy
```

- Defined in live.ts:128

Settings

On This Page

Constructors

Properties

Methods

- Loading...

Generated using TypeDoc

---

## GenerateImagesParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.GenerateImagesParameters.html

# Interface GenerateImagesParameters

The parameters for generating images.

- Defined in types.ts:2393

Index

### Properties

Properties

### Optionalconfig

Configuration for generating images.

- Defined in types.ts:2402

### model

ID of the model to use. For a list of models, see Google models &lt;https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models&gt;\_.

- Defined in types.ts:2396

### prompt

Text prompt that typically describes the images to output.

- Defined in types.ts:2399

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## GenerateVideosParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.GenerateVideosParameters.html

# Interface GenerateVideosParameters

Class that represents the parameters for generating an image.

- Defined in types.ts:2898

Index

### Properties

Properties

### Optionalconfig

Configuration for generating videos.

- Defined in types.ts:2908

### Optionalimage

The input image for generating the videos.
Optional if prompt is provided.

- Defined in types.ts:2906

### model

ID of the model to use. For a list of models, see Google models &lt;https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models&gt;\_.

- Defined in types.ts:2901

### Optionalprompt

The text prompt for generating the videos. Optional for image to video use cases.

- Defined in types.ts:2903

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Caches | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/caches.Caches.html#delete

# Class Caches

#### Hierarchy

- BaseModule
    - Caches

- Defined in caches.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Caches ( apiClient : ApiClient ) : Caches Parameters Returns Caches Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Caches

Overrides BaseModule.constructor

- Defined in caches.ts:17

Methods

### create

- create ( params : CreateCachedContentParameters ) : Promise &lt; CachedContent &gt; Creates a cached contents resource. Parameters Returns Promise &lt; CachedContent &gt; The created cached content. Remarks Context caching is only supported for specific models. See GeminiDeveloper API reference and Vertex AI reference for more information. Example const contents = ...; // Initialize the content to cache. const response = await ai . caches . create ({ model: 'gemini-2.0-flash-001' , config: { 'contents' : contents , 'displayName' : 'test cache' , 'systemInstruction' : 'What is the sum of the two pdfs?' , 'ttl' : '86400s' , } }); Copy
- Creates a cached contents resource.

#### Parameters

- params: CreateCachedContentParametersThe parameters for the create request.

#### Returns Promise&lt;CachedContent&gt;

The created cached content.

#### Remarks

Context caching is only supported for specific models. See Gemini
Developer API reference
and Vertex AI reference
for more information.

#### Example

```
const contents = ...; // Initialize the content to cache.
const response = await ai.caches.create({
  model: 'gemini-2.0-flash-001',
  config: {
   'contents': contents,
   'displayName': 'test cache',
   'systemInstruction': 'What is the sum of the two pdfs?',
   'ttl': '86400s',
 }
});
Copy
```

- Defined in caches.ts:72

### delete

- delete ( params : DeleteCachedContentParameters , ) : Promise &lt; DeleteCachedContentResponse &gt; Deletes cached content. Parameters Returns Promise &lt; DeleteCachedContentResponse &gt; The empty response returned by the API. Example await ai . caches . delete ({ name: '...' }); // The server-generated resource name. Copy
- Deletes cached content.

#### Parameters

- params: DeleteCachedContentParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteCachedContentResponse&gt;

The empty response returned by the API.

#### Example

```
await ai.caches.delete({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:252

### get

- get ( params : GetCachedContentParameters ) : Promise &lt; CachedContent &gt; Gets cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The cached content. Example await ai . caches . get ({ name: '...' }); // The server-generated resource name. Copy
- Gets cached content configurations.

#### Parameters

- params: GetCachedContentParametersThe parameters for the get request.

#### Returns Promise&lt;CachedContent&gt;

The cached content.

#### Example

```
await ai.caches.get({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:162

### list

- list ( params ?: ListCachedContentsParameters ) : Promise &lt; Pager &lt; CachedContent &gt; &gt; Lists cached content configurations. Parameters Returns Promise &lt; Pager &lt; CachedContent &gt; &gt; The paginated results of the list of cached contents. Example const cachedContents = await ai . caches . list ({ config: { 'pageSize' : 2 }}); for ( const cachedContent of cachedContents ) { console . log ( cachedContent ); } Copy
- Lists cached content configurations.

#### Parameters

- params: ListCachedContentsParameters = {}The parameters for the list request.

#### Returns Promise&lt;Pager&lt;CachedContent&gt;&gt;

The paginated results of the list of cached contents.

#### Example

```
const cachedContents = await ai.caches.list({config: {'pageSize': 2}});
for (const cachedContent of cachedContents) {
  console.log(cachedContent);
}
Copy
```

- Defined in caches.ts:35

### update

- update ( params : UpdateCachedContentParameters ) : Promise &lt; CachedContent &gt; Updates cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The updated cached content. Example const response = await ai . caches . update ({ name: '...' , // The server-generated resource name. config: { 'ttl' : '7600s' } }); Copy
- Updates cached content configurations.

#### Parameters

- params: UpdateCachedContentParametersThe parameters for the update request.

#### Returns Promise&lt;CachedContent&gt;

The updated cached content.

#### Example

```
const response = await ai.caches.update({
  name: '...',  // The server-generated resource name.
  config: {'ttl': '7600s'}
});
Copy
```

- Defined in caches.ts:341

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Session | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/live.Session.html

# Class SessionExperimental

Represents a connection to the API.

- Defined in live.ts:273

Index

### Constructors

### Properties

### Methods

Constructors

### constructor

- new Session ( conn : WebSocket , apiClient : ApiClient ) : Session Experimental Parameters Returns Session
- ```
Experimental
```

#### Parameters

- conn: WebSocket
- apiClient: ApiClient

#### Returns Session

- Defined in live.ts:274

Properties

### Readonly Experimentalconn

- Defined in live.ts:275

Methods

### close

- close () : void Experimental Terminates the WebSocket connection. Returns void Example let model : string ; if ( GOOGLE\_GENAI\_USE\_VERTEXAI ) { model = 'gemini-2.0-flash-live-preview-04-09' ; } else { model = 'gemini-2.0-flash-live-001' ; } const session = await ai . live . connect ({ model: model , config: { responseModalities: [ Modality . AUDIO ], } }); session . close (); Copy
- ```
Experimental
```
- Terminates the WebSocket connection.

#### Returns void

#### Example

```
let model: string;
if (GOOGLE_GENAI_USE_VERTEXAI) {
  model = 'gemini-2.0-flash-live-preview-04-09';
} else {
  model = 'gemini-2.0-flash-live-001';
}
const session = await ai.live.connect({
  model: model,
  config: {
    responseModalities: [Modality.AUDIO],
  }
});

session.close();
Copy
```

- Defined in live.ts:504

### sendClientContent

- sendClientContent ( params : LiveSendClientContentParameters ) : void Experimental Send a message over the established connection. Parameters Returns void Remarks There are two ways to send messages to the live API:sendClientContent and sendRealtimeInput . sendClientContent messages are added to the model context in order .Having a conversation using sendClientContent messages is roughlyequivalent to using the Chat.sendMessageStream , except that the state ofthe chat history is stored on the API server instead of locally. Because of sendClientContent 's order guarantee, the model cannot responsas quickly to sendClientContent messages as to sendRealtimeInput messages. This makes the biggest difference when sending objects that havesignificant preprocessing time (typically images). The sendClientContent message sends a Content[] which has more options than the Blob sent by sendRealtimeInput . So the main use-cases for sendClientContent over sendRealtimeInput are:
- ```
Experimental
```
- Send a message over the established connection.

#### Parameters

- params : LiveSendClientContentParameters Contains two optional properties, turns andturnComplete .
- Contains two optional properties, turns and
turnComplete.
    - turns will be converted to a Content[]
    - turnComplete: true [default] indicates that you are done sending
content and expect a response. If turnComplete: false, the server
will wait for additional messages before starting generation.

#### Returns void

#### Remarks

There are two ways to send messages to the live API:
sendClientContent and sendRealtimeInput.

sendClientContent messages are added to the model context in order.
Having a conversation using sendClientContent messages is roughly
equivalent to using the Chat.sendMessageStream, except that the state of
the chat history is stored on the API server instead of locally.

Because of sendClientContent's order guarantee, the model cannot respons
as quickly to sendClientContent messages as to sendRealtimeInput
messages. This makes the biggest difference when sending objects that have
significant preprocessing time (typically images).

The sendClientContent message sends a Content[]
which has more options than the Blob sent by sendRealtimeInput.

So the main use-cases for sendClientContent over sendRealtimeInput are:

- Sending anything that can't be represented as a Blob (text,
sendClientContent({turns="Hello?"})).
- Managing turns when not using audio input and voice activity detection.
(sendClientContent({turnComplete:true}) or the short form
sendClientContent())
- Prefilling a conversation contextsendClientContent({
    turns: [
      Content({role:user, parts:...}),
      Content({role:user, parts:...}),
      ...
    ]
})
Copy

- Defined in live.ts:401

### sendRealtimeInput

- sendRealtimeInput ( params : LiveSendRealtimeInputParameters ) : void Experimental Send a realtime message over the established connection. Parameters Returns void Remarks Use sendRealtimeInput for realtime audio chunks and video frames (images). With sendRealtimeInput the api will respond to audio automaticallybased on voice activity detection (VAD). sendRealtimeInput is optimized for responsivness at the expense ofdeterministic ordering guarantees. Audio and video tokens are to thecontext when they become available. Note: The Call signature expects a Blob object, but only a subsetof audio and image mimetypes are allowed.
- ```
Experimental
```
- Send a realtime message over the established connection.

#### Parameters

- params : LiveSendRealtimeInputParameters Contains one property, media .
- Contains one property, media.
    - media will be converted to a Blob

#### Returns void

#### Remarks

Use sendRealtimeInput for realtime audio chunks and video frames (images).

With sendRealtimeInput the api will respond to audio automatically
based on voice activity detection (VAD).

sendRealtimeInput is optimized for responsivness at the expense of
deterministic ordering guarantees. Audio and video tokens are to the
context when they become available.

Note: The Call signature expects a Blob object, but only a subset
of audio and image mimetypes are allowed.

- Defined in live.ts:436

### sendToolResponse

- sendToolResponse ( params : LiveSendToolResponseParameters ) : void Experimental Send a function response message over the established connection. Parameters Returns void Remarks Use sendFunctionResponse to reply to LiveServerToolCall from the server. Use types.LiveConnectConfig#tools to configure the callable functions.
- ```
Experimental
```
- Send a function response message over the established connection.

#### Parameters

- params : LiveSendToolResponseParameters Contains property functionResponses .
- Contains property functionResponses.
    - functionResponses will be converted to a functionResponses[]

#### Returns void

#### Remarks

Use sendFunctionResponse to reply to LiveServerToolCall from the server.

Use types.LiveConnectConfig#tools to configure the callable functions.

- Defined in live.ts:471

Settings

On This Page

Constructors

Properties

Methods

- Loading...

Generated using TypeDoc

---

## Chats | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/chats.Chats.html

# Class Chats

A utility class to create a chat session.

- Defined in chats.ts:104

Index

### Constructors

### Methods

Constructors

### constructor

- new Chats ( modelsModule : Models , apiClient : ApiClient ) : Chats Parameters Returns Chats

#### Parameters

- modelsModule: Models
- apiClient: ApiClient

#### Returns Chats

- Defined in chats.ts:108

Methods

### create

- create ( params : CreateChatParameters ) : Chat Creates a new chat session. Parameters Returns Chat A new chat session. Remarks The config in the params will be used for all requests within the chatsession unless overridden by a per-request config in See types.SendMessageParameters#config . Example const chat = ai . chats . create ({ model: 'gemini-2.0-flash' config : { temperature: 0.5 , maxOutputTokens: 1024 , } }); Copy
- Creates a new chat session.

#### Parameters

- params: CreateChatParametersParameters for creating a chat session.

#### Returns Chat

A new chat session.

#### Remarks

The config in the params will be used for all requests within the chat
session unless overridden by a per-request config in

#### See

types.SendMessageParameters#config.

#### Example

```
const chat = ai.chats.create({
  model: 'gemini-2.0-flash'
  config: {
    temperature: 0.5,
    maxOutputTokens: 1024,
  }
});
Copy
```

- Defined in chats.ts:135

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## LiveMusic | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/music.LiveMusic.html

# Class LiveMusicExperimental

LiveMusic class encapsulates the configuration for live music
generation via Lyria Live models.

- Defined in music.ts:57

Index

### Constructors

### Methods

Constructors

### constructor

- new LiveMusic ( apiClient : ApiClient , auth : Auth , webSocketFactory : WebSocketFactory , ) : LiveMusic Experimental Parameters Returns LiveMusic
- ```
Experimental
```

#### Parameters

- apiClient: ApiClient
- auth: Auth
- webSocketFactory: WebSocketFactory

#### Returns LiveMusic

- Defined in music.ts:58

Methods

### connect

- connect ( params : LiveMusicConnectParameters ) : Promise &lt; LiveMusicSession &gt; Experimental Establishes a connection to the specified model and returns aLiveMusicSession object representing that connection. Parameters Returns Promise &lt; LiveMusicSession &gt; A live session. Remarks Example let model = 'models/lyria-realtime-exp' ; const session = await ai . live . music . connect ({ model: model , callbacks: { onmessage : ( e : MessageEvent ) =&gt; { console . log ( 'Received message from the server: %s \n ' , debug ( e . data )); }, onerror : ( e : ErrorEvent ) =&gt; { console . log ( 'Error occurred: %s \n ' , debug ( e . error )); }, onclose : ( e : CloseEvent ) =&gt; { console . log ( 'Connection closed.' ); }, }, }); Copy
- ```
Experimental
```
- Establishes a connection to the specified model and returns a
LiveMusicSession object representing that connection.

#### Parameters

- params: LiveMusicConnectParametersThe parameters for establishing a connection to the model.

#### Returns Promise&lt;LiveMusicSession&gt;

A live session.

#### Remarks

#### Example

```
let model = 'models/lyria-realtime-exp';
const session = await ai.live.music.connect({
  model: model,
  callbacks: {
    onmessage: (e: MessageEvent) => {
      console.log('Received message from the server: %s\n', debug(e.data));
    },
    onerror: (e: ErrorEvent) => {
      console.log('Error occurred: %s\n', debug(e.error));
    },
    onclose: (e: CloseEvent) => {
      console.log('Connection closed.');
    },
  },
});
Copy
```

- Defined in music.ts:94

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## CachedContent | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.CachedContent.html

# Interface CachedContent

A resource used in LLM queries for users to explicitly specify what to cache.

- Defined in types.ts:3411

Index

### Properties

Properties

### OptionalcreateTime

Creation time of the cache entry.

- Defined in types.ts:3419

### OptionaldisplayName

The user-generated meaningful display name of the cached content.

- Defined in types.ts:3415

### OptionalexpireTime

Expiration time of the cached content.

- Defined in types.ts:3423

### Optionalmodel

The name of the publisher model to use for cached content.

- Defined in types.ts:3417

### Optionalname

The server-generated resource name of the cached content.

- Defined in types.ts:3413

### OptionalupdateTime

When the cache entry was last updated in UTC time.

- Defined in types.ts:3421

### OptionalusageMetadata

Metadata on the usage of the cached content.

- Defined in types.ts:3425

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## EmbedContentParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.EmbedContentParameters.html

# Interface EmbedContentParameters

Parameters for the embed\_content method.

- Defined in types.ts:2275

Index

### Properties

Properties

### Optionalconfig

Configuration that contains optional parameters.

- Defined in types.ts:2284

### contents

The content to embed. Only the parts.text fields will be counted.

- Defined in types.ts:2281

### model

ID of the model to use. For a list of models, see Google models &lt;https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models&gt;\_.

- Defined in types.ts:2278

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Model | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.Model.html

# Interface Model

A trained machine learning model.

- Defined in types.ts:2624

Index

### Properties

Properties

### Optionalcheckpoints

The checkpoints of the model.

- Defined in types.ts:2653

### OptionaldefaultCheckpointId

The default checkpoint id of a model version.

- Defined in types.ts:2651

### Optionaldescription

Description of the model.

- Defined in types.ts:2630

### OptionaldisplayName

Display name of the model.

- Defined in types.ts:2628

### Optionalendpoints

List of deployed models created from this base model. Note that a
model could have been deployed to endpoints in different locations.

- Defined in types.ts:2638

### OptionalinputTokenLimit

The maximum number of input tokens that the model can handle.

- Defined in types.ts:2644

### Optionallabels

Labels with user-defined metadata to organize your models.

- Defined in types.ts:2640

### Optionalname

Resource name of the model.

- Defined in types.ts:2626

### OptionaloutputTokenLimit

The maximum number of output tokens that the model can generate.

- Defined in types.ts:2646

### OptionalsupportedActions

List of actions that are supported by the model.

- Defined in types.ts:2648

### OptionaltunedModelInfo

Information about the tuned model from the base model.

- Defined in types.ts:2642

### Optionalversion

Version ID of the model. A new version is committed when a new
model version is uploaded or trained under an existing model ID. The
version ID is an auto-incrementing decimal number in string
representation.

- Defined in types.ts:2635

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#computetokens

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## EditImageParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.EditImageParameters.html

# Interface EditImageParameters

Parameters for the request to edit an image.

- Defined in types.ts:2229

Index

### Properties

Properties

### Optionalconfig

Configuration for editing.

- Defined in types.ts:2237

### model

The model to use.

- Defined in types.ts:2231

### prompt

A text description of the edit to apply to the image.

- Defined in types.ts:2233

### referenceImages

The reference images for Imagen 3 editing.

- Defined in types.ts:2235

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#generatecontentstream

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Caches | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/caches.Caches.html#get

# Class Caches

#### Hierarchy

- BaseModule
    - Caches

- Defined in caches.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Caches ( apiClient : ApiClient ) : Caches Parameters Returns Caches Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Caches

Overrides BaseModule.constructor

- Defined in caches.ts:17

Methods

### create

- create ( params : CreateCachedContentParameters ) : Promise &lt; CachedContent &gt; Creates a cached contents resource. Parameters Returns Promise &lt; CachedContent &gt; The created cached content. Remarks Context caching is only supported for specific models. See GeminiDeveloper API reference and Vertex AI reference for more information. Example const contents = ...; // Initialize the content to cache. const response = await ai . caches . create ({ model: 'gemini-2.0-flash-001' , config: { 'contents' : contents , 'displayName' : 'test cache' , 'systemInstruction' : 'What is the sum of the two pdfs?' , 'ttl' : '86400s' , } }); Copy
- Creates a cached contents resource.

#### Parameters

- params: CreateCachedContentParametersThe parameters for the create request.

#### Returns Promise&lt;CachedContent&gt;

The created cached content.

#### Remarks

Context caching is only supported for specific models. See Gemini
Developer API reference
and Vertex AI reference
for more information.

#### Example

```
const contents = ...; // Initialize the content to cache.
const response = await ai.caches.create({
  model: 'gemini-2.0-flash-001',
  config: {
   'contents': contents,
   'displayName': 'test cache',
   'systemInstruction': 'What is the sum of the two pdfs?',
   'ttl': '86400s',
 }
});
Copy
```

- Defined in caches.ts:72

### delete

- delete ( params : DeleteCachedContentParameters , ) : Promise &lt; DeleteCachedContentResponse &gt; Deletes cached content. Parameters Returns Promise &lt; DeleteCachedContentResponse &gt; The empty response returned by the API. Example await ai . caches . delete ({ name: '...' }); // The server-generated resource name. Copy
- Deletes cached content.

#### Parameters

- params: DeleteCachedContentParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteCachedContentResponse&gt;

The empty response returned by the API.

#### Example

```
await ai.caches.delete({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:252

### get

- get ( params : GetCachedContentParameters ) : Promise &lt; CachedContent &gt; Gets cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The cached content. Example await ai . caches . get ({ name: '...' }); // The server-generated resource name. Copy
- Gets cached content configurations.

#### Parameters

- params: GetCachedContentParametersThe parameters for the get request.

#### Returns Promise&lt;CachedContent&gt;

The cached content.

#### Example

```
await ai.caches.get({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:162

### list

- list ( params ?: ListCachedContentsParameters ) : Promise &lt; Pager &lt; CachedContent &gt; &gt; Lists cached content configurations. Parameters Returns Promise &lt; Pager &lt; CachedContent &gt; &gt; The paginated results of the list of cached contents. Example const cachedContents = await ai . caches . list ({ config: { 'pageSize' : 2 }}); for ( const cachedContent of cachedContents ) { console . log ( cachedContent ); } Copy
- Lists cached content configurations.

#### Parameters

- params: ListCachedContentsParameters = {}The parameters for the list request.

#### Returns Promise&lt;Pager&lt;CachedContent&gt;&gt;

The paginated results of the list of cached contents.

#### Example

```
const cachedContents = await ai.caches.list({config: {'pageSize': 2}});
for (const cachedContent of cachedContents) {
  console.log(cachedContent);
}
Copy
```

- Defined in caches.ts:35

### update

- update ( params : UpdateCachedContentParameters ) : Promise &lt; CachedContent &gt; Updates cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The updated cached content. Example const response = await ai . caches . update ({ name: '...' , // The server-generated resource name. config: { 'ttl' : '7600s' } }); Copy
- Updates cached content configurations.

#### Parameters

- params: UpdateCachedContentParametersThe parameters for the update request.

#### Returns Promise&lt;CachedContent&gt;

The updated cached content.

#### Example

```
const response = await ai.caches.update({
  name: '...',  // The server-generated resource name.
  config: {'ttl': '7600s'}
});
Copy
```

- Defined in caches.ts:341

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#update

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## UpdateCachedContentParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.UpdateCachedContentParameters.html

# Interface UpdateCachedContentParameters

- Defined in types.ts:3494

Index

### Properties

Properties

### Optionalconfig

Configuration that contains optional parameters.

- Defined in types.ts:3500

### name

The server-generated resource name of the cached content.

- Defined in types.ts:3497

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#embedcontent

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/models.html

# Module models

Classes

Settings

On This Page

Classes

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#generateimages

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Caches | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/caches.Caches.html

# Class Caches

#### Hierarchy

- BaseModule
    - Caches

- Defined in caches.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Caches ( apiClient : ApiClient ) : Caches Parameters Returns Caches Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Caches

Overrides BaseModule.constructor

- Defined in caches.ts:17

Methods

### create

- create ( params : CreateCachedContentParameters ) : Promise &lt; CachedContent &gt; Creates a cached contents resource. Parameters Returns Promise &lt; CachedContent &gt; The created cached content. Remarks Context caching is only supported for specific models. See GeminiDeveloper API reference and Vertex AI reference for more information. Example const contents = ...; // Initialize the content to cache. const response = await ai . caches . create ({ model: 'gemini-2.0-flash-001' , config: { 'contents' : contents , 'displayName' : 'test cache' , 'systemInstruction' : 'What is the sum of the two pdfs?' , 'ttl' : '86400s' , } }); Copy
- Creates a cached contents resource.

#### Parameters

- params: CreateCachedContentParametersThe parameters for the create request.

#### Returns Promise&lt;CachedContent&gt;

The created cached content.

#### Remarks

Context caching is only supported for specific models. See Gemini
Developer API reference
and Vertex AI reference
for more information.

#### Example

```
const contents = ...; // Initialize the content to cache.
const response = await ai.caches.create({
  model: 'gemini-2.0-flash-001',
  config: {
   'contents': contents,
   'displayName': 'test cache',
   'systemInstruction': 'What is the sum of the two pdfs?',
   'ttl': '86400s',
 }
});
Copy
```

- Defined in caches.ts:72

### delete

- delete ( params : DeleteCachedContentParameters , ) : Promise &lt; DeleteCachedContentResponse &gt; Deletes cached content. Parameters Returns Promise &lt; DeleteCachedContentResponse &gt; The empty response returned by the API. Example await ai . caches . delete ({ name: '...' }); // The server-generated resource name. Copy
- Deletes cached content.

#### Parameters

- params: DeleteCachedContentParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteCachedContentResponse&gt;

The empty response returned by the API.

#### Example

```
await ai.caches.delete({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:252

### get

- get ( params : GetCachedContentParameters ) : Promise &lt; CachedContent &gt; Gets cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The cached content. Example await ai . caches . get ({ name: '...' }); // The server-generated resource name. Copy
- Gets cached content configurations.

#### Parameters

- params: GetCachedContentParametersThe parameters for the get request.

#### Returns Promise&lt;CachedContent&gt;

The cached content.

#### Example

```
await ai.caches.get({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:162

### list

- list ( params ?: ListCachedContentsParameters ) : Promise &lt; Pager &lt; CachedContent &gt; &gt; Lists cached content configurations. Parameters Returns Promise &lt; Pager &lt; CachedContent &gt; &gt; The paginated results of the list of cached contents. Example const cachedContents = await ai . caches . list ({ config: { 'pageSize' : 2 }}); for ( const cachedContent of cachedContents ) { console . log ( cachedContent ); } Copy
- Lists cached content configurations.

#### Parameters

- params: ListCachedContentsParameters = {}The parameters for the list request.

#### Returns Promise&lt;Pager&lt;CachedContent&gt;&gt;

The paginated results of the list of cached contents.

#### Example

```
const cachedContents = await ai.caches.list({config: {'pageSize': 2}});
for (const cachedContent of cachedContents) {
  console.log(cachedContent);
}
Copy
```

- Defined in caches.ts:35

### update

- update ( params : UpdateCachedContentParameters ) : Promise &lt; CachedContent &gt; Updates cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The updated cached content. Example const response = await ai . caches . update ({ name: '...' , // The server-generated resource name. config: { 'ttl' : '7600s' } }); Copy
- Updates cached content configurations.

#### Parameters

- params: UpdateCachedContentParametersThe parameters for the update request.

#### Returns Promise&lt;CachedContent&gt;

The updated cached content.

#### Example

```
const response = await ai.caches.update({
  name: '...',  // The server-generated resource name.
  config: {'ttl': '7600s'}
});
Copy
```

- Defined in caches.ts:341

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#delete

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## GetCachedContentParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.GetCachedContentParameters.html

# Interface GetCachedContentParameters

Parameters for caches.get method.

- Defined in types.ts:3442

Index

### Properties

Properties

### Optionalconfig

Optional parameters for the request.

- Defined in types.ts:3448

### name

The server-generated resource name of the cached content.

- Defined in types.ts:3445

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules.html

# @google/genai

Modules

Settings

On This Page

Modules

- Loading...

Generated using TypeDoc

---

## @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/index.html

# @google/genai

# Google Gen AI SDK for TypeScript and JavaScript

Documentation: https://googleapis.github.io/js-genai/

The Google Gen AI JavaScript SDK is designed for
TypeScript and JavaScript developers to build applications powered by Gemini. The SDK
supports both the Gemini Developer API
and Vertex AI.

The Google Gen AI SDK is designed to work with Gemini 2.0 features.

API Key Security: Avoid exposing API keys in client-side code.
Use server-side implementations in production environments.

## Prerequisites

- Node.js version 18 or later

## Installation

To install the SDK, run the following command:

```
npm install @google/genai
Copy
```

## Quickstart

The simplest way to get started is to using an API key from
Google AI Studio:

```
import {GoogleGenAI} from '@google/genai';
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

const ai = new GoogleGenAI({apiKey: GEMINI_API_KEY});

async function main() {
  const response = await ai.models.generateContent({
    model: 'gemini-2.0-flash-001',
    contents: 'Why is the sky blue?',
  });
  console.log(response.text);
}

main();
Copy
```

## Initialization

The Google Gen AI SDK provides support for both the
Google AI Studio and
Vertex AI
implementations of the Gemini API.

### Gemini Developer API

For server-side applications, initialize using an API key, which can
be acquired from Google AI Studio:

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({apiKey: 'GEMINI_API_KEY'});
Copy
```

#### Browser

API Key Security: Avoid exposing API keys in client-side code.
Use server-side implementations in production environments.

In the browser the initialization code is identical:

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({apiKey: 'GEMINI_API_KEY'});
Copy
```

### Vertex AI

Sample code for VertexAI initialization:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({
    vertexai: true,
    project: 'your_project',
    location: 'your_location',
});
Copy
```

## API Selection

By default, the SDK uses the beta API endpoints provided by Google to support
preview features in the APIs. The stable API endpoints can be selected by
setting the API version to v1.

To set the API version use apiVersion. For example, to set the API version to
v1 for Vertex AI:

```
const ai = new GoogleGenAI({
    vertexai: true,
    project: 'your_project',
    location: 'your_location',
    apiVersion: 'v1'
});
Copy
```

To set the API version to v1alpha for the Gemini Developer API:

```
const ai = new GoogleGenAI({
    apiKey: 'GEMINI_API_KEY',
    apiVersion: 'v1alpha'
});
Copy
```

## GoogleGenAI overview

All API features are accessed through an instance of the GoogleGenAI classes.
The submodules bundle together related API methods:

- ai.models:
Use models to query models (generateContent, generateImages, ...), or
examine their metadata.
- ai.caches:
Create and manage caches to reduce costs when repeatedly using the same
large prompt prefix.
- ai.chats:
Create local stateful chat objects to simplify multi turn interactions.
- ai.files:
Upload files to the API and reference them in your prompts.
This reduces bandwidth if you use a file many times, and handles files too
large to fit inline with your prompt.
- ai.live:
Start a live session for real time interaction, allows text + audio + video
input, and text or audio output.

## Samples

More samples can be found in the
github samples directory.

### Streaming

For quicker, more responsive API interactions use the generateContentStream
method which yields chunks as they're generated:

```
import {GoogleGenAI} from '@google/genai';
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

const ai = new GoogleGenAI({apiKey: GEMINI_API_KEY});

async function main() {
  const response = await ai.models.generateContentStream({
    model: 'gemini-2.0-flash-001',
    contents: 'Write a 100-word poem.',
  });
  for await (const chunk of response) {
    console.log(chunk.text);
  }
}

main();
Copy
```

### Function Calling

To let Gemini to interact with external systems, you can provide provide
functionDeclaration objects as tools. To use these tools it's a 4 step

1. Declare the function name, description, and parameters
2. Call generateContent with function calling enabled
3. Use the returned FunctionCall parameters to call your actual function
4. Send the result back to the model (with history, easier in ai.chat)
as a FunctionResponse

```
import {GoogleGenAI, FunctionCallingConfigMode, FunctionDeclaration, Type} from '@google/genai';
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

async function main() {
  const controlLightDeclaration: FunctionDeclaration = {
    name: 'controlLight',
    parameters: {
      type: Type.OBJECT,
      description: 'Set the brightness and color temperature of a room light.',
      properties: {
        brightness: {
          type: Type.NUMBER,
          description:
              'Light level from 0 to 100. Zero is off and 100 is full brightness.',
        },
        colorTemperature: {
          type: Type.STRING,
          description:
              'Color temperature of the light fixture which can be `daylight`, `cool`, or `warm`.',
        },
      },
      required: ['brightness', 'colorTemperature'],
    },
  };

  const ai = new GoogleGenAI({apiKey: GEMINI_API_KEY});
  const response = await ai.models.generateContent({
    model: 'gemini-2.0-flash-001',
    contents: 'Dim the lights so the room feels cozy and warm.',
    config: {
      toolConfig: {
        functionCallingConfig: {
          // Force it to call any function
          mode: FunctionCallingConfigMode.ANY,
          allowedFunctionNames: ['controlLight'],
        }
      },
      tools: [{functionDeclarations: [controlLightDeclaration]}]
    }
  });

  console.log(response.functionCalls);
}

main();
Copy
```

### Generate Content

#### How to structure contents argument for generateContent

The SDK allows you to specify the following types in the contents parameter:

#### Content

- Content: The SDK will wrap the singular Content instance in an array which
contains only the given content instance
- Content[]: No transformation happens

#### Part

Parts will be aggregated on a singular Content, with role 'user'.

- Part | string: The SDK will wrap the string or Part in a Content
instance with role 'user'.
- Part[] | string[]: The SDK will wrap the full provided list into a single
Content with role 'user'.

NOTE: This doesn't apply to FunctionCall and FunctionResponse parts,
if you are specifying those, you need to explicitly provide the full
Content[] structure making it explicit which Parts are 'spoken' by the model,
or the user. The SDK will throw an exception if you try this.

## How is this different from the other Google AI SDKs

This SDK (@google/genai) is Google Deepmind’s "vanilla" SDK for its generative
AI offerings, and is where Google Deepmind adds new AI features.

Models hosted either on the Vertex AI platform or the Gemini Developer platform are accessible through this SDK.

Other SDKs may be offering additional AI frameworks on top of this SDK, or may
be targeting specific project environments (like Firebase).

The @google/generative\_language and @google-cloud/vertexai SDKs are previous
iterations of this SDK and are no longer receiving new Gemini 2.0+ features.

Settings

On This Page

- Prerequisites
- Installation
- Quickstart
- Initialization
    - Gemini Developer API
        - Browser
    - Vertex AI
- API Selection
- GoogleGenAI overview
- Samples
    - Streaming
    - Function Calling
    - Generate Content
        - How to structure contents argument for generateContent
        - Content
        - Part
- How is this different from the other Google AI SDKs

- Loading...

Generated using TypeDoc

---

## live | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/live.html

# Module live

Classes

Settings

On This Page

Classes

- Loading...

Generated using TypeDoc

---

## Chats | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/chats.Chats.html#create

# Class Chats

A utility class to create a chat session.

- Defined in chats.ts:104

Index

### Constructors

### Methods

Constructors

### constructor

- new Chats ( modelsModule : Models , apiClient : ApiClient ) : Chats Parameters Returns Chats

#### Parameters

- modelsModule: Models
- apiClient: ApiClient

#### Returns Chats

- Defined in chats.ts:108

Methods

### create

- create ( params : CreateChatParameters ) : Chat Creates a new chat session. Parameters Returns Chat A new chat session. Remarks The config in the params will be used for all requests within the chatsession unless overridden by a per-request config in See types.SendMessageParameters#config . Example const chat = ai . chats . create ({ model: 'gemini-2.0-flash' config : { temperature: 0.5 , maxOutputTokens: 1024 , } }); Copy
- Creates a new chat session.

#### Parameters

- params: CreateChatParametersParameters for creating a chat session.

#### Returns Chat

A new chat session.

#### Remarks

The config in the params will be used for all requests within the chat
session unless overridden by a per-request config in

#### See

types.SendMessageParameters#config.

#### Example

```
const chat = ai.chats.create({
  model: 'gemini-2.0-flash'
  config: {
    temperature: 0.5,
    maxOutputTokens: 1024,
  }
});
Copy
```

- Defined in chats.ts:135

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## CreateCachedContentParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.CreateCachedContentParameters.html

# Interface CreateCachedContentParameters

Parameters for caches.create method.

- Defined in types.ts:3388

Index

### Properties

Properties

### Optionalconfig

Configuration that contains optional parameters.

- Defined in types.ts:3393

### model

ID of the model to use. Example: gemini-2.0-flash

- Defined in types.ts:3390

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## operations | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/operations.html

# Module operations

Classes

Settings

On This Page

Classes

- Loading...

Generated using TypeDoc

---

## Chat | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/chats.Chat.html

# Class Chat

Chat session that enables sending messages to the model with previous
conversation context.

#### Remarks

The session maintains all the turns between user and model.

- Defined in chats.ts:155

Index

### Constructors

### Methods

Constructors

### constructor

- new Chat ( apiClient : ApiClient , modelsModule : Models , model : string , config ?: GenerateContentConfig , history ?: Content [] , ) : Chat Parameters Returns Chat

#### Parameters

- apiClient: ApiClient
- modelsModule: Models
- model: string
- config: GenerateContentConfig = {}
- history: Content[] = []

#### Returns Chat

- Defined in chats.ts:160

Methods

### getHistory

- getHistory ( curated ?: boolean ) : Content [] Returns the chat history. Parameters Returns Content [] History contents alternating between user and model for the entirechat session. Remarks The history is a list of contents alternating between user and model. There are two types of history: The history is updated after receiving the response from the model,for streaming response, it means receiving the last chunk of the response. The comprehensive history is returned by default. To get the curated history , set the curated parameter to true .
- Returns the chat history.

#### Parameters

- curated: boolean = falsewhether to return the curated history or the comprehensive
history.

#### Returns Content[]

History contents alternating between user and model for the entire
chat session.

#### Remarks

The history is a list of contents alternating between user and model.

There are two types of history:

- The curated history contains only the valid turns between user and
model, which will be included in the subsequent requests sent to the model.
- The comprehensive history contains all turns, including invalid or
empty model outputs, providing a complete record of the history.

The history is updated after receiving the response from the model,
for streaming response, it means receiving the last chunk of the response.

The comprehensive history is returned by default. To get the curated history, set the curated parameter to true.

- Defined in chats.ts:298

### sendMessage

- sendMessage ( params : SendMessageParameters ) : Promise &lt; GenerateContentResponse &gt; Sends a message to the model and returns the response. Parameters Returns Promise &lt; GenerateContentResponse &gt; The model's response. Remarks This method will wait for the previous message to be processed beforesending the next message. See Chat#sendMessageStream for streaming method. Example const chat = ai . chats . create ({ model: 'gemini-2.0-flash' }); const response = await chat . sendMessage ({ message: 'Why is the sky blue?' }); console . log ( response . text ); Copy
- Sends a message to the model and returns the response.

#### Parameters

- params: SendMessageParametersparameters for sending messages within a chat session.

#### Returns Promise&lt;GenerateContentResponse&gt;

The model's response.

#### Remarks

This method will wait for the previous message to be processed before
sending the next message.

#### See

Chat#sendMessageStream for streaming method.

#### Example

```
const chat = ai.chats.create({model: 'gemini-2.0-flash'});
const response = await chat.sendMessage({
  message: 'Why is the sky blue?'
});
console.log(response.text);
Copy
```

- Defined in chats.ts:190

### sendMessageStream

- sendMessageStream ( params : SendMessageParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Sends a message to the model and returns the response in chunks. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The model's response. Remarks This method will wait for the previous message to be processed beforesending the next message. See Chat#sendMessage for non-streaming method. Example const chat = ai . chats . create ({ model: 'gemini-2.0-flash' }); const response = await chat . sendMessageStream ({ message: 'Why is the sky blue?' }); for await ( const chunk of response ) { console . log ( chunk . text ); } Copy
- Sends a message to the model and returns the response in chunks.

#### Parameters

- params: SendMessageParametersparameters for sending the message.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The model's response.

#### Remarks

This method will wait for the previous message to be processed before
sending the next message.

#### See

Chat#sendMessage for non-streaming method.

#### Example

```
const chat = ai.chats.create({model: 'gemini-2.0-flash'});
const response = await chat.sendMessageStream({
  message: 'Why is the sky blue?'
});
for await (const chunk of response) {
  console.log(chunk.text);
}
Copy
```

- Defined in chats.ts:254

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## UploadFileParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.UploadFileParameters.html#config

# Interface UploadFileParameters

Parameters for the upload file method.

- Defined in types.ts:4808

Index

### Properties

Properties

### Optionalconfig

Configuration that contains optional parameters.

- Defined in types.ts:4812

### file

The string path to the file to be uploaded or a Blob object.

- Defined in types.ts:4810

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## ListFilesParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.ListFilesParameters.html

# Interface ListFilesParameters

Generates the parameters for the list method.

- Defined in types.ts:3548

Index

### Properties

Properties

### Optionalconfig

Used to override the default configuration.

- Defined in types.ts:3550

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## client | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/client.html

# Module client

Classes

Interfaces

Settings

On This Page

Classes

Interfaces

- Loading...

Generated using TypeDoc

---

## SendMessageParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.SendMessageParameters.html#config

# Interface SendMessageParameters

Parameters for sending a message within a chat session.

These parameters are used with the chat.sendMessage() method.

- Defined in types.ts:4620

Index

### Properties

Properties

### Optionalconfig

Config for this specific request.

Please note that the per-request config does not change the chat level
config, nor inherit from it. If you intend to use some values from the
chat's default config, you must explicitly copy them into this per-request
config.

- Defined in types.ts:4634

### message

The message to send to the model.

The SDK will combine all parts into a single 'user' content to send to
the model.

- Defined in types.ts:4626

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## EditImageResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.EditImageResponse.html

# Class EditImageResponse

Response for the request to edit an image.

- Defined in types.ts:2563

Index

### Constructors

### Properties

Constructors

### constructor

- new EditImageResponse(): EditImageResponseReturns EditImageResponse

Properties

### OptionalgeneratedImages

Generated images.

- Defined in types.ts:2565

Settings

On This Page

Constructors

Properties

- Loading...

Generated using TypeDoc

---

## pagers | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/pagers.html

# Module pagers

Enumerations

Classes

Settings

On This Page

Enumerations

Classes

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#generatecontent

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## files | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/files.html

# Module files

Classes

Settings

On This Page

Classes

- Loading...

Generated using TypeDoc

---

## Redirecting...

**Source URL:** https://googleapis.github.io/js-genai/

# Redirecting...

If you are not redirected automatically,
    click here to go to the release version docs.

---

## Files | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/files.Files.html#list

# Class Files

#### Hierarchy

- BaseModule
    - Files

- Defined in files.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Files ( apiClient : ApiClient ) : Files Parameters Returns Files Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Files

Overrides BaseModule.constructor

- Defined in files.ts:17

Methods

### delete

- delete ( params : DeleteFileParameters ) : Promise &lt; DeleteFileResponse &gt; Deletes a remotely stored file. Parameters Returns Promise &lt; DeleteFileResponse &gt; The DeleteFileResponse, the response for the delete method. Example The following code deletes an example file named "files/mehozpxf877d". await ai . files . delete ({ name: file . name }); Copy
- Deletes a remotely stored file.

#### Parameters

- params: DeleteFileParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteFileResponse&gt;

The DeleteFileResponse, the response for the delete method.

#### Example

The following code deletes an example file named "files/mehozpxf877d".

```
await ai.files.delete({name: file.name});
Copy
```

- Defined in files.ts:288

### download

- download ( params : DownloadFileParameters ) : Promise &lt; void &gt; Downloads a remotely stored file asynchronously to a location specified inthe params object. This method only works on Node environment, todownload files in the browser, use a browser compliant method like an tag. Parameters Returns Promise &lt; void &gt; Example The following code downloads an example file named "files/mehozpxf877d" as"file.txt". await ai . files . download ({ file: file . name , downloadPath: 'file.txt' }); Copy
- Downloads a remotely stored file asynchronously to a location specified in
the params object. This method only works on Node environment, to
download files in the browser, use a browser compliant method like an 
tag.

#### Parameters

- params: DownloadFileParametersThe parameters for the download request.

#### Returns Promise&lt;void&gt;

#### Example

The following code downloads an example file named "files/mehozpxf877d" as
"file.txt".

```
await ai.files.download({file: file.name, downloadPath: 'file.txt'});
Copy
```

- Defined in files.ts:124

### get

- get ( params : GetFileParameters ) : Promise &lt; File &gt; Retrieves the file information from the service. Parameters Returns Promise &lt; File &gt; The Promise that resolves to the types.File object requested. Example const config : GetFileParameters = { name: fileName , }; file = await ai . files . get ( config ); console . log ( file . name ); Copy
- Retrieves the file information from the service.

#### Parameters

- params: GetFileParametersThe parameters for the get request

#### Returns Promise&lt;File&gt;

The Promise that resolves to the types.File object requested.

#### Example

```
const config: GetFileParameters = {
  name: fileName,
};
file = await ai.files.get(config);
console.log(file.name);
Copy
```

- Defined in files.ts:235

### list

- list ( params ?: ListFilesParameters ) : Promise &lt; Pager &lt; File &gt; &gt; Lists all current project files from the service. Parameters Returns Promise &lt; Pager &lt; File &gt; &gt; The paginated results of the list of files Example The following code prints the names of all files from the service, thesize of each page is 10. const listResponse = await ai . files . list ({ config: { 'pageSize' : 10 }}); for await ( const file of listResponse ) { console . log ( file . name ); } Copy
- Lists all current project files from the service.

#### Parameters

- params: ListFilesParameters = {}The parameters for the list request

#### Returns Promise&lt;Pager&lt;File&gt;&gt;

The paginated results of the list of files

#### Example

The following code prints the names of all files from the service, the
size of each page is 10.

```
const listResponse = await ai.files.list({config: {'pageSize': 10}});
for await (const file of listResponse) {
  console.log(file.name);
}
Copy
```

- Defined in files.ts:38

### upload

- upload ( params : UploadFileParameters ) : Promise &lt; File &gt; Uploads a file asynchronously to the Gemini API.This method is not available in Vertex AI.Supported upload sources: Parameters Returns Promise &lt; File &gt; A promise that resolves to a types.File object. Remarks The mimeType can be specified in the config parameter. If omitted: This section can contain multiple paragraphs and code examples. See types.UploadFileParameters#config for the optionalconfig in the parameters. Throws An error if called on a Vertex AI client. Throws An error if the mimeType is not provided and can not be inferred,the mimeType can be provided in the params.config parameter. Throws An error occurs if a suitable upload location cannot be established. Example The following code uploads a file to Gemini API. const file = await ai . files . upload ({ file: 'file.txt' , config: { mimeType: 'text/plain' , }}); console . log ( file . name ); Copy
- Uploads a file asynchronously to the Gemini API.
This method is not available in Vertex AI.
Supported upload sources:
    - Node.js: File path (string) or Blob object.
    - Browser: Blob object (e.g., File).

#### Parameters

- params: UploadFileParametersOptional parameters specified in the
types.UploadFileParameters interface.

#### Returns Promise&lt;File&gt;

A promise that resolves to a types.File object.

#### Remarks

The mimeType can be specified in the config parameter. If omitted:

- For file path (string) inputs, the mimeType will be inferred from the
file extension.
- For Blob object inputs, the mimeType will be set to the Blob's type
property.
Somex eamples for file extension to mimeType mapping:
.txt -&gt; text/plain
.json -&gt; application/json
.jpg  -&gt; image/jpeg
.png -&gt; image/png
.mp3 -&gt; audio/mpeg
.mp4 -&gt; video/mp4

This section can contain multiple paragraphs and code examples.

#### See

types.UploadFileParameters#config for the optional
config in the parameters.

#### Throws

An error if called on a Vertex AI client.

#### Throws

An error if the mimeType is not provided and can not be inferred,
the mimeType can be provided in the params.config parameter.

#### Throws

An error occurs if a suitable upload location cannot be established.

#### Example

The following code uploads a file to Gemini API.

```
const file = await ai.files.upload({file: 'file.txt', config: {
  mimeType: 'text/plain',
}});
console.log(file.name);
Copy
```

- Defined in files.ts:92

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## ComputeTokensParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.ComputeTokensParameters.html

# Interface ComputeTokensParameters

Parameters for computing tokens.

- Defined in types.ts:2835

Index

### Properties

Properties

### Optionalconfig

Optional parameters for the request.

- Defined in types.ts:2843

### contents

Input content.

- Defined in types.ts:2840

### model

ID of the model to use. For a list of models, see Google models &lt;https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models&gt;\_.

- Defined in types.ts:2838

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Caches | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/caches.Caches.html#update

# Class Caches

#### Hierarchy

- BaseModule
    - Caches

- Defined in caches.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Caches ( apiClient : ApiClient ) : Caches Parameters Returns Caches Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Caches

Overrides BaseModule.constructor

- Defined in caches.ts:17

Methods

### create

- create ( params : CreateCachedContentParameters ) : Promise &lt; CachedContent &gt; Creates a cached contents resource. Parameters Returns Promise &lt; CachedContent &gt; The created cached content. Remarks Context caching is only supported for specific models. See GeminiDeveloper API reference and Vertex AI reference for more information. Example const contents = ...; // Initialize the content to cache. const response = await ai . caches . create ({ model: 'gemini-2.0-flash-001' , config: { 'contents' : contents , 'displayName' : 'test cache' , 'systemInstruction' : 'What is the sum of the two pdfs?' , 'ttl' : '86400s' , } }); Copy
- Creates a cached contents resource.

#### Parameters

- params: CreateCachedContentParametersThe parameters for the create request.

#### Returns Promise&lt;CachedContent&gt;

The created cached content.

#### Remarks

Context caching is only supported for specific models. See Gemini
Developer API reference
and Vertex AI reference
for more information.

#### Example

```
const contents = ...; // Initialize the content to cache.
const response = await ai.caches.create({
  model: 'gemini-2.0-flash-001',
  config: {
   'contents': contents,
   'displayName': 'test cache',
   'systemInstruction': 'What is the sum of the two pdfs?',
   'ttl': '86400s',
 }
});
Copy
```

- Defined in caches.ts:72

### delete

- delete ( params : DeleteCachedContentParameters , ) : Promise &lt; DeleteCachedContentResponse &gt; Deletes cached content. Parameters Returns Promise &lt; DeleteCachedContentResponse &gt; The empty response returned by the API. Example await ai . caches . delete ({ name: '...' }); // The server-generated resource name. Copy
- Deletes cached content.

#### Parameters

- params: DeleteCachedContentParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteCachedContentResponse&gt;

The empty response returned by the API.

#### Example

```
await ai.caches.delete({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:252

### get

- get ( params : GetCachedContentParameters ) : Promise &lt; CachedContent &gt; Gets cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The cached content. Example await ai . caches . get ({ name: '...' }); // The server-generated resource name. Copy
- Gets cached content configurations.

#### Parameters

- params: GetCachedContentParametersThe parameters for the get request.

#### Returns Promise&lt;CachedContent&gt;

The cached content.

#### Example

```
await ai.caches.get({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:162

### list

- list ( params ?: ListCachedContentsParameters ) : Promise &lt; Pager &lt; CachedContent &gt; &gt; Lists cached content configurations. Parameters Returns Promise &lt; Pager &lt; CachedContent &gt; &gt; The paginated results of the list of cached contents. Example const cachedContents = await ai . caches . list ({ config: { 'pageSize' : 2 }}); for ( const cachedContent of cachedContents ) { console . log ( cachedContent ); } Copy
- Lists cached content configurations.

#### Parameters

- params: ListCachedContentsParameters = {}The parameters for the list request.

#### Returns Promise&lt;Pager&lt;CachedContent&gt;&gt;

The paginated results of the list of cached contents.

#### Example

```
const cachedContents = await ai.caches.list({config: {'pageSize': 2}});
for (const cachedContent of cachedContents) {
  console.log(cachedContent);
}
Copy
```

- Defined in caches.ts:35

### update

- update ( params : UpdateCachedContentParameters ) : Promise &lt; CachedContent &gt; Updates cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The updated cached content. Example const response = await ai . caches . update ({ name: '...' , // The server-generated resource name. config: { 'ttl' : '7600s' } }); Copy
- Updates cached content configurations.

#### Parameters

- params: UpdateCachedContentParametersThe parameters for the update request.

#### Returns Promise&lt;CachedContent&gt;

The updated cached content.

#### Example

```
const response = await ai.caches.update({
  name: '...',  // The server-generated resource name.
  config: {'ttl': '7600s'}
});
Copy
```

- Defined in caches.ts:341

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## GetFileParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.GetFileParameters.html

# Interface GetFileParameters

Generates the parameters for the get method.

- Defined in types.ts:3695

Index

### Properties

Properties

### Optionalconfig

Used to override the default configuration.

- Defined in types.ts:3699

### name

The name identifier for the file to retrieve.

- Defined in types.ts:3697

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#upscaleimage

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## GetModelParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.GetModelParameters.html

# Interface GetModelParameters

- Defined in types.ts:2586

Index

### Properties

Properties

### Optionalconfig

Optional parameters for the request.

- Defined in types.ts:2589

### model

- Defined in types.ts:2587

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## GenerateContentParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.GenerateContentParameters.html

# Interface GenerateContentParameters

Config for models.generate\_content parameters.

- Defined in types.ts:1667

Index

### Properties

Properties

### Optionalconfig

Configuration that contains optional model parameters.

- Defined in types.ts:1676

### contents

Content of the request.

- Defined in types.ts:1673

### model

ID of the model to use. For a list of models, see Google models &lt;https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models&gt;\_.

- Defined in types.ts:1670

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Pager | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/pagers.Pager.html

# Class Pager&lt;T&gt;

Pager class for iterating through paginated results.

#### Type Parameters

- T

#### Implements

- AsyncIterable&lt;T&gt;

- Defined in pagers.ts:38

Index

### Constructors

### Accessors

### Methods

Constructors

### constructor

- new Pager &lt; T &gt; ( name : PagedItem , request : ( params : PagedItemConfig ) =&gt; Promise &lt; PagedItemResponse &lt; T &gt; &gt; , response : PagedItemResponse &lt; T &gt; , params : PagedItemConfig , ) : Pager &lt; T &gt; Type Parameters Parameters Returns Pager &lt; T &gt;

#### Type Parameters

- T

#### Parameters

- name: PagedItem
- request: (params: PagedItemConfig) =&gt; Promise&lt;PagedItemResponse&lt;T&gt;&gt;
- response: PagedItemResponse&lt;T&gt;
- params: PagedItemConfig

#### Returns Pager&lt;T&gt;

- Defined in pagers.ts:48

Accessors

### name

- get name () : PagedItem Returns the type of paged item (for example, batch\_jobs ). Returns PagedItem
- Returns the type of paged item (for example, batch\_jobs).

#### Returns PagedItem

- Defined in pagers.ts:100

### page

- get page () : T [] Returns the current page, which is a list of items. Returns T [] Remarks The first page is retrieved when the pager is created. The returned list ofitems could be a subset of the entire list.
- Returns the current page, which is a list of items.

#### Returns T[]

#### Remarks

The first page is retrieved when the pager is created. The returned list of
items could be a subset of the entire list.

- Defined in pagers.ts:93

### pageLength

- get pageLength () : number Returns the total number of items in the current page. Returns number
- Returns the total number of items in the current page.

#### Returns number

- Defined in pagers.ts:129

### pageSize

- get pageSize () : number Returns the length of the page fetched each time by this pager. Returns number Remarks The number of items in the page is less than or equal to the page length.
- Returns the length of the page fetched each time by this pager.

#### Returns number

#### Remarks

The number of items in the page is less than or equal to the page length.

- Defined in pagers.ts:110

### params

- get params () : PagedItemConfig Returns the parameters when making the API request for the next page. Returns PagedItemConfig Remarks Parameters contain a set of optional configs that can beused to customize the API request. For example, the pageToken parametercontains the token to request the next page.
- Returns the parameters when making the API request for the next page.

#### Returns PagedItemConfig

#### Remarks

Parameters contain a set of optional configs that can be
used to customize the API request. For example, the pageToken parameter
contains the token to request the next page.

- Defined in pagers.ts:122

Methods

### [asyncIterator]

- "[asyncIterator]" () : AsyncIterator &lt; T &gt; Returns an async iterator that support iterating through all itemsretrieved from the API. Returns AsyncIterator &lt; T &gt; Remarks The iterator will automatically fetch the next page if there are more itemsto fetch from the API. Example const pager = await ai . files . list ({ config: { pageSize: 10 }}); for await ( const file of pager ) { console . log ( file . name ); } Copy Implementation of AsyncIterable.[asyncIterator]
- Returns an async iterator that support iterating through all items
retrieved from the API.

#### Returns AsyncIterator&lt;T&gt;

#### Remarks

The iterator will automatically fetch the next page if there are more items
to fetch from the API.

#### Example

```
const pager = await ai.files.list({config: {pageSize: 10}});
for await (const file of pager) {
  console.log(file.name);
}
Copy
```

Implementation of AsyncIterable.[asyncIterator]

- Defined in pagers.ts:157

### getItem

- getItem ( index : number ) : T Returns the item at the given index. Parameters Returns T
- Returns the item at the given index.

#### Parameters

- index: number

#### Returns T

- Defined in pagers.ts:136

### hasNextPage

- hasNextPage () : boolean Returns true if there are more pages to fetch from the API. Returns boolean
- Returns true if there are more pages to fetch from the API.

#### Returns boolean

- Defined in pagers.ts:210

### nextPage

- nextPage () : Promise &lt; T [] &gt; Fetches the next page of items. This makes a new API request. Returns Promise &lt; T [] &gt; Throws If there are no more pages to fetch. Example const pager = await ai . files . list ({ config: { pageSize: 10 }}); let page = pager . page ; while ( true ) { for ( const file of page ) { console . log ( file . name ); } if (! pager . hasNextPage ()) { break ; } page = await pager . nextPage (); } Copy
- Fetches the next page of items. This makes a new API request.

#### Returns Promise&lt;T[]&gt;

#### Throws

If there are no more pages to fetch.

#### Example

```
const pager = await ai.files.list({config: {pageSize: 10}});
let page = pager.page;
while (true) {
  for (const file of page) {
    console.log(file.name);
  }
  if (!pager.hasNextPage()) {
    break;
  }
  page = await pager.nextPage();
}
Copy
```

- Defined in pagers.ts:198

Settings

On This Page

Constructors

Accessors

Methods

- Loading...

Generated using TypeDoc

---

## UpscaleImageResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.UpscaleImageResponse.html

# Class UpscaleImageResponse

- Defined in types.ts:2568

Index

### Constructors

### Properties

Constructors

### constructor

- new UpscaleImageResponse(): UpscaleImageResponseReturns UpscaleImageResponse

Properties

### OptionalgeneratedImages

Generated images.

- Defined in types.ts:2570

Settings

On This Page

Constructors

Properties

- Loading...

Generated using TypeDoc

---

## CreateChatParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.CreateChatParameters.html

# Interface CreateChatParameters

Parameters for initializing a new chat session.

These parameters are used when creating a chat session with the
chats.create() method.

- Defined in types.ts:4594

Index

### Properties

Properties

### Optionalconfig

Config for the entire chat session.

This config applies to all requests within the session
unless overridden by a per-request config in SendMessageParameters.

- Defined in types.ts:4606

### Optionalhistory

The initial conversation history for the chat session.

This allows you to start the chat with a pre-existing history. The history
must be a list of Content alternating between 'user' and 'model' roles.
It should start with a 'user' message.

- Defined in types.ts:4613

### model

The name of the model to use for the chat session.

For example: 'gemini-2.0-flash', 'gemini-2.0-flash-lite', etc. See Gemini API
docs to find the available models.

- Defined in types.ts:4600

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## Files | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/files.Files.html#constructor

# Class Files

#### Hierarchy

- BaseModule
    - Files

- Defined in files.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Files ( apiClient : ApiClient ) : Files Parameters Returns Files Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Files

Overrides BaseModule.constructor

- Defined in files.ts:17

Methods

### delete

- delete ( params : DeleteFileParameters ) : Promise &lt; DeleteFileResponse &gt; Deletes a remotely stored file. Parameters Returns Promise &lt; DeleteFileResponse &gt; The DeleteFileResponse, the response for the delete method. Example The following code deletes an example file named "files/mehozpxf877d". await ai . files . delete ({ name: file . name }); Copy
- Deletes a remotely stored file.

#### Parameters

- params: DeleteFileParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteFileResponse&gt;

The DeleteFileResponse, the response for the delete method.

#### Example

The following code deletes an example file named "files/mehozpxf877d".

```
await ai.files.delete({name: file.name});
Copy
```

- Defined in files.ts:288

### download

- download ( params : DownloadFileParameters ) : Promise &lt; void &gt; Downloads a remotely stored file asynchronously to a location specified inthe params object. This method only works on Node environment, todownload files in the browser, use a browser compliant method like an tag. Parameters Returns Promise &lt; void &gt; Example The following code downloads an example file named "files/mehozpxf877d" as"file.txt". await ai . files . download ({ file: file . name , downloadPath: 'file.txt' }); Copy
- Downloads a remotely stored file asynchronously to a location specified in
the params object. This method only works on Node environment, to
download files in the browser, use a browser compliant method like an 
tag.

#### Parameters

- params: DownloadFileParametersThe parameters for the download request.

#### Returns Promise&lt;void&gt;

#### Example

The following code downloads an example file named "files/mehozpxf877d" as
"file.txt".

```
await ai.files.download({file: file.name, downloadPath: 'file.txt'});
Copy
```

- Defined in files.ts:124

### get

- get ( params : GetFileParameters ) : Promise &lt; File &gt; Retrieves the file information from the service. Parameters Returns Promise &lt; File &gt; The Promise that resolves to the types.File object requested. Example const config : GetFileParameters = { name: fileName , }; file = await ai . files . get ( config ); console . log ( file . name ); Copy
- Retrieves the file information from the service.

#### Parameters

- params: GetFileParametersThe parameters for the get request

#### Returns Promise&lt;File&gt;

The Promise that resolves to the types.File object requested.

#### Example

```
const config: GetFileParameters = {
  name: fileName,
};
file = await ai.files.get(config);
console.log(file.name);
Copy
```

- Defined in files.ts:235

### list

- list ( params ?: ListFilesParameters ) : Promise &lt; Pager &lt; File &gt; &gt; Lists all current project files from the service. Parameters Returns Promise &lt; Pager &lt; File &gt; &gt; The paginated results of the list of files Example The following code prints the names of all files from the service, thesize of each page is 10. const listResponse = await ai . files . list ({ config: { 'pageSize' : 10 }}); for await ( const file of listResponse ) { console . log ( file . name ); } Copy
- Lists all current project files from the service.

#### Parameters

- params: ListFilesParameters = {}The parameters for the list request

#### Returns Promise&lt;Pager&lt;File&gt;&gt;

The paginated results of the list of files

#### Example

The following code prints the names of all files from the service, the
size of each page is 10.

```
const listResponse = await ai.files.list({config: {'pageSize': 10}});
for await (const file of listResponse) {
  console.log(file.name);
}
Copy
```

- Defined in files.ts:38

### upload

- upload ( params : UploadFileParameters ) : Promise &lt; File &gt; Uploads a file asynchronously to the Gemini API.This method is not available in Vertex AI.Supported upload sources: Parameters Returns Promise &lt; File &gt; A promise that resolves to a types.File object. Remarks The mimeType can be specified in the config parameter. If omitted: This section can contain multiple paragraphs and code examples. See types.UploadFileParameters#config for the optionalconfig in the parameters. Throws An error if called on a Vertex AI client. Throws An error if the mimeType is not provided and can not be inferred,the mimeType can be provided in the params.config parameter. Throws An error occurs if a suitable upload location cannot be established. Example The following code uploads a file to Gemini API. const file = await ai . files . upload ({ file: 'file.txt' , config: { mimeType: 'text/plain' , }}); console . log ( file . name ); Copy
- Uploads a file asynchronously to the Gemini API.
This method is not available in Vertex AI.
Supported upload sources:
    - Node.js: File path (string) or Blob object.
    - Browser: Blob object (e.g., File).

#### Parameters

- params: UploadFileParametersOptional parameters specified in the
types.UploadFileParameters interface.

#### Returns Promise&lt;File&gt;

A promise that resolves to a types.File object.

#### Remarks

The mimeType can be specified in the config parameter. If omitted:

- For file path (string) inputs, the mimeType will be inferred from the
file extension.
- For Blob object inputs, the mimeType will be set to the Blob's type
property.
Somex eamples for file extension to mimeType mapping:
.txt -&gt; text/plain
.json -&gt; application/json
.jpg  -&gt; image/jpeg
.png -&gt; image/png
.mp3 -&gt; audio/mpeg
.mp4 -&gt; video/mp4

This section can contain multiple paragraphs and code examples.

#### See

types.UploadFileParameters#config for the optional
config in the parameters.

#### Throws

An error if called on a Vertex AI client.

#### Throws

An error if the mimeType is not provided and can not be inferred,
the mimeType can be provided in the params.config parameter.

#### Throws

An error occurs if a suitable upload location cannot be established.

#### Example

The following code uploads a file to Gemini API.

```
const file = await ai.files.upload({file: 'file.txt', config: {
  mimeType: 'text/plain',
}});
console.log(file.name);
Copy
```

- Defined in files.ts:92

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Files | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/files.Files.html#delete

# Class Files

#### Hierarchy

- BaseModule
    - Files

- Defined in files.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Files ( apiClient : ApiClient ) : Files Parameters Returns Files Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Files

Overrides BaseModule.constructor

- Defined in files.ts:17

Methods

### delete

- delete ( params : DeleteFileParameters ) : Promise &lt; DeleteFileResponse &gt; Deletes a remotely stored file. Parameters Returns Promise &lt; DeleteFileResponse &gt; The DeleteFileResponse, the response for the delete method. Example The following code deletes an example file named "files/mehozpxf877d". await ai . files . delete ({ name: file . name }); Copy
- Deletes a remotely stored file.

#### Parameters

- params: DeleteFileParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteFileResponse&gt;

The DeleteFileResponse, the response for the delete method.

#### Example

The following code deletes an example file named "files/mehozpxf877d".

```
await ai.files.delete({name: file.name});
Copy
```

- Defined in files.ts:288

### download

- download ( params : DownloadFileParameters ) : Promise &lt; void &gt; Downloads a remotely stored file asynchronously to a location specified inthe params object. This method only works on Node environment, todownload files in the browser, use a browser compliant method like an tag. Parameters Returns Promise &lt; void &gt; Example The following code downloads an example file named "files/mehozpxf877d" as"file.txt". await ai . files . download ({ file: file . name , downloadPath: 'file.txt' }); Copy
- Downloads a remotely stored file asynchronously to a location specified in
the params object. This method only works on Node environment, to
download files in the browser, use a browser compliant method like an 
tag.

#### Parameters

- params: DownloadFileParametersThe parameters for the download request.

#### Returns Promise&lt;void&gt;

#### Example

The following code downloads an example file named "files/mehozpxf877d" as
"file.txt".

```
await ai.files.download({file: file.name, downloadPath: 'file.txt'});
Copy
```

- Defined in files.ts:124

### get

- get ( params : GetFileParameters ) : Promise &lt; File &gt; Retrieves the file information from the service. Parameters Returns Promise &lt; File &gt; The Promise that resolves to the types.File object requested. Example const config : GetFileParameters = { name: fileName , }; file = await ai . files . get ( config ); console . log ( file . name ); Copy
- Retrieves the file information from the service.

#### Parameters

- params: GetFileParametersThe parameters for the get request

#### Returns Promise&lt;File&gt;

The Promise that resolves to the types.File object requested.

#### Example

```
const config: GetFileParameters = {
  name: fileName,
};
file = await ai.files.get(config);
console.log(file.name);
Copy
```

- Defined in files.ts:235

### list

- list ( params ?: ListFilesParameters ) : Promise &lt; Pager &lt; File &gt; &gt; Lists all current project files from the service. Parameters Returns Promise &lt; Pager &lt; File &gt; &gt; The paginated results of the list of files Example The following code prints the names of all files from the service, thesize of each page is 10. const listResponse = await ai . files . list ({ config: { 'pageSize' : 10 }}); for await ( const file of listResponse ) { console . log ( file . name ); } Copy
- Lists all current project files from the service.

#### Parameters

- params: ListFilesParameters = {}The parameters for the list request

#### Returns Promise&lt;Pager&lt;File&gt;&gt;

The paginated results of the list of files

#### Example

The following code prints the names of all files from the service, the
size of each page is 10.

```
const listResponse = await ai.files.list({config: {'pageSize': 10}});
for await (const file of listResponse) {
  console.log(file.name);
}
Copy
```

- Defined in files.ts:38

### upload

- upload ( params : UploadFileParameters ) : Promise &lt; File &gt; Uploads a file asynchronously to the Gemini API.This method is not available in Vertex AI.Supported upload sources: Parameters Returns Promise &lt; File &gt; A promise that resolves to a types.File object. Remarks The mimeType can be specified in the config parameter. If omitted: This section can contain multiple paragraphs and code examples. See types.UploadFileParameters#config for the optionalconfig in the parameters. Throws An error if called on a Vertex AI client. Throws An error if the mimeType is not provided and can not be inferred,the mimeType can be provided in the params.config parameter. Throws An error occurs if a suitable upload location cannot be established. Example The following code uploads a file to Gemini API. const file = await ai . files . upload ({ file: 'file.txt' , config: { mimeType: 'text/plain' , }}); console . log ( file . name ); Copy
- Uploads a file asynchronously to the Gemini API.
This method is not available in Vertex AI.
Supported upload sources:
    - Node.js: File path (string) or Blob object.
    - Browser: Blob object (e.g., File).

#### Parameters

- params: UploadFileParametersOptional parameters specified in the
types.UploadFileParameters interface.

#### Returns Promise&lt;File&gt;

A promise that resolves to a types.File object.

#### Remarks

The mimeType can be specified in the config parameter. If omitted:

- For file path (string) inputs, the mimeType will be inferred from the
file extension.
- For Blob object inputs, the mimeType will be set to the Blob's type
property.
Somex eamples for file extension to mimeType mapping:
.txt -&gt; text/plain
.json -&gt; application/json
.jpg  -&gt; image/jpeg
.png -&gt; image/png
.mp3 -&gt; audio/mpeg
.mp4 -&gt; video/mp4

This section can contain multiple paragraphs and code examples.

#### See

types.UploadFileParameters#config for the optional
config in the parameters.

#### Throws

An error if called on a Vertex AI client.

#### Throws

An error if the mimeType is not provided and can not be inferred,
the mimeType can be provided in the params.config parameter.

#### Throws

An error occurs if a suitable upload location cannot be established.

#### Example

The following code uploads a file to Gemini API.

```
const file = await ai.files.upload({file: 'file.txt', config: {
  mimeType: 'text/plain',
}});
console.log(file.name);
Copy
```

- Defined in files.ts:92

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Live | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/live.Live.html#constructor

# Class LiveExperimental

Live class encapsulates the configuration for live interaction with the
Generative Language API. It embeds ApiClient for general API settings.

- Defined in live.ts:71

Index

### Constructors

### Properties

### Methods

Constructors

### constructor

- new Live ( apiClient : ApiClient , auth : Auth , webSocketFactory : WebSocketFactory , ) : Live Experimental Parameters Returns Live
- ```
Experimental
```

#### Parameters

- apiClient: ApiClient
- auth: Auth
- webSocketFactory: WebSocketFactory

#### Returns Live

- Defined in live.ts:74

Properties

### Readonly Experimentalmusic

- Defined in live.ts:72

Methods

### connect

- connect ( params : LiveConnectParameters ) : Promise &lt; Session &gt; Experimental Establishes a connection to the specified model with the givenconfiguration and returns a Session object representing that connection. Built-in MCP support is an experimental feature, may change infuture versions. Parameters Returns Promise &lt; Session &gt; A live session. Remarks Example let model : string ; if ( GOOGLE\_GENAI\_USE\_VERTEXAI ) { model = 'gemini-2.0-flash-live-preview-04-09' ; } else { model = 'gemini-2.0-flash-live-001' ; } const session = await ai . live . connect ({ model: model , config: { responseModalities: [ Modality . AUDIO ], }, callbacks: { onopen : () =&gt; { console . log ( 'Connected to the socket.' ); }, onmessage : ( e : MessageEvent ) =&gt; { console . log ( 'Received message from the server: %s \n ' , debug ( e . data )); }, onerror : ( e : ErrorEvent ) =&gt; { console . log ( 'Error occurred: %s \n ' , debug ( e . error )); }, onclose : ( e : CloseEvent ) =&gt; { console . log ( 'Connection closed.' ); }, }, }); Copy
- ```
Experimental
```
- Establishes a connection to the specified model with the given
configuration and returns a Session object representing that connection.
- Built-in MCP support is an experimental feature, may change in
future versions.

#### Parameters

- params: LiveConnectParametersThe parameters for establishing a connection to the model.

#### Returns Promise&lt;Session&gt;

A live session.

#### Remarks

#### Example

```
let model: string;
if (GOOGLE_GENAI_USE_VERTEXAI) {
  model = 'gemini-2.0-flash-live-preview-04-09';
} else {
  model = 'gemini-2.0-flash-live-001';
}
const session = await ai.live.connect({
  model: model,
  config: {
    responseModalities: [Modality.AUDIO],
  },
  callbacks: {
    onopen: () => {
      console.log('Connected to the socket.');
    },
    onmessage: (e: MessageEvent) => {
      console.log('Received message from the server: %s\n', debug(e.data));
    },
    onerror: (e: ErrorEvent) => {
      console.log('Error occurred: %s\n', debug(e.error));
    },
    onclose: (e: CloseEvent) => {
      console.log('Connection closed.');
    },
  },
});
Copy
```

- Defined in live.ts:128

Settings

On This Page

Constructors

Properties

Methods

- Loading...

Generated using TypeDoc

---

## Models | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/models.Models.html#constructor

# Class Models

#### Hierarchy

- BaseModule
    - Models

- Defined in models.ts:30

Index

### Constructors

### Methods

Constructors

### constructor

- new Models ( apiClient : ApiClient ) : Models Parameters Returns Models Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Models

Overrides BaseModule.constructor

- Defined in models.ts:31

Methods

### computeTokens

- computeTokens ( params : ComputeTokensParameters ) : Promise &lt; ComputeTokensResponse &gt; Given a list of contents, returns a corresponding TokensInfo containingthe list of tokens and list of token ids. This method is not supported by the Gemini Developer API. Parameters Returns Promise &lt; ComputeTokensResponse &gt; The response from the API. Example const response = await ai . models . computeTokens ({ model: 'gemini-2.0-flash' , contents: 'What is your name?' }); console . log ( response ); Copy
- Given a list of contents, returns a corresponding TokensInfo containing
the list of tokens and list of token ids.
- This method is not supported by the Gemini Developer API.

#### Parameters

- params: ComputeTokensParametersThe parameters for computing tokens.

#### Returns Promise&lt;ComputeTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.computeTokens({
 model: 'gemini-2.0-flash',
 contents: 'What is your name?'
});
console.log(response);
Copy
```

- Defined in models.ts:1431

### countTokens

- countTokens ( params : CountTokensParameters ) : Promise &lt; CountTokensResponse &gt; Counts the number of tokens in the given contents. Multimodal input issupported for Gemini models. Parameters Returns Promise &lt; CountTokensResponse &gt; The response from the API. Example const response = await ai . models . countTokens ({ model: 'gemini-2.0-flash' , contents: 'The quick brown fox jumps over the lazy dog.' }); console . log ( response ); Copy
- Counts the number of tokens in the given contents. Multimodal input is
supported for Gemini models.

#### Parameters

- params: CountTokensParametersThe parameters for counting tokens.

#### Returns Promise&lt;CountTokensResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.countTokens({
 model: 'gemini-2.0-flash',
 contents: 'The quick brown fox jumps over the lazy dog.'
});
console.log(response);
Copy
```

- Defined in models.ts:1332

### delete

- delete ( params : DeleteModelParameters ) : Promise &lt; DeleteModelResponse &gt; Deletes a tuned model by its name. Parameters Returns Promise &lt; DeleteModelResponse &gt; The response from the API. Example const response = await ai . models . delete ({ model: 'tuned-model-name' }); Copy
- Deletes a tuned model by its name.

#### Parameters

- params: DeleteModelParametersThe parameters for deleting the model.

#### Returns Promise&lt;DeleteModelResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.delete({model: 'tuned-model-name'});
Copy
```

- Defined in models.ts:1241

### editImage

- editImage ( params : EditImageParameters ) : Promise &lt; EditImageResponse &gt; Edits an image based on a prompt, list of reference images, and configuration. Parameters Returns Promise &lt; EditImageResponse &gt; The response from the API. Example const response = await client . models . editImage ({ model: 'imagen-3.0-capability-001' , prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.' , referenceImages: [ subjectReferenceImage ] config : { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Edits an image based on a prompt, list of reference images, and configuration.

#### Parameters

- params: EditImageParametersThe parameters for editing an image.

#### Returns Promise&lt;EditImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.editImage({
 model: 'imagen-3.0-capability-001',
 prompt: 'Generate an image containing a mug with the product logo [1] visible on the side of the mug.',
 referenceImages: [subjectReferenceImage]
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:465

### embedContent

- embedContent ( params : EmbedContentParameters ) : Promise &lt; EmbedContentResponse &gt; Calculates embeddings for the given contents. Only text is supported. Parameters Returns Promise &lt; EmbedContentResponse &gt; The response from the API. Example const response = await ai . models . embedContent ({ model: 'text-embedding-004' , contents: [ 'What is your name?' , 'What is your favorite color?' , ], config: { outputDimensionality: 64 , }, }); console . log ( response ); Copy
- Calculates embeddings for the given contents. Only text is supported.

#### Parameters

- params: EmbedContentParametersThe parameters for embedding contents.

#### Returns Promise&lt;EmbedContentResponse&gt;

The response from the API.

#### Example

```
const response = await ai.models.embedContent({
 model: 'text-embedding-004',
 contents: [
   'What is your name?',
   'What is your favorite color?',
 ],
 config: {
   outputDimensionality: 64,
 },
});
console.log(response);
Copy
```

- Defined in models.ts:710

### generateContent

- generateContent ( params : GenerateContentParameters , ) : Promise &lt; GenerateContentResponse &gt; Makes an API request to generate content with a given model. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; GenerateContentResponse &gt; The response from generating content. Example const response = await ai . models . generateContent ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { candidateCount: 2 , } }); console . log ( response ); Copy
- Makes an API request to generate content with a given model.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content.

#### Returns Promise&lt;GenerateContentResponse&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContent({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    candidateCount: 2,
  }
});
console.log(response);
Copy
```

- Defined in models.ts:73

### generateContentStream

- generateContentStream ( params : GenerateContentParameters , ) : Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; Makes an API request to generate content with a given model and yields theresponse in chunks. For the model parameter, supported formats for Vertex AI API include: For the model parameter, supported formats for Gemini API include: Some models support multimodal input and output. Parameters Returns Promise &lt; AsyncGenerator &lt; GenerateContentResponse , any , unknown &gt; &gt; The response from generating content. Example const response = await ai . models . generateContentStream ({ model: 'gemini-2.0-flash' , contents: 'why is the sky blue?' , config: { maxOutputTokens: 200 , } }); for await ( const chunk of response ) { console . log ( chunk ); } Copy
- Makes an API request to generate content with a given model and yields the
response in chunks.
- For the model parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
'publishers/google/models/gemini-2.0-flash' or
'publishers/meta/models/llama-3.1-405b-instruct-maas'
    - / separated publisher and model name, for example:
'google/gemini-2.0-flash' or 'meta/llama-3.1-405b-instruct-maas'
- For the model parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
for example:
'tunedModels/1234567890123456789'
- Some models support multimodal input and output.

#### Parameters

- params: GenerateContentParametersThe parameters for generating content with streaming response.

#### Returns Promise&lt;AsyncGenerator&lt;GenerateContentResponse, any, unknown&gt;&gt;

The response from generating content.

#### Example

```
const response = await ai.models.generateContentStream({
  model: 'gemini-2.0-flash',
  contents: 'why is the sky blue?',
  config: {
    maxOutputTokens: 200,
  }
});
for await (const chunk of response) {
  console.log(chunk);
}
Copy
```

- Defined in models.ts:183

### generateImages

- generateImages ( params : GenerateImagesParameters , ) : Promise &lt; GenerateImagesResponse &gt; Generates an image based on a text description and configuration. Parameters Returns Promise &lt; GenerateImagesResponse &gt; The response from the API. Example const response = await client . models . generateImages ({ model: 'imagen-3.0-generate-002' , prompt: 'Robot holding a red skateboard' , config: { numberOfImages: 1 , includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Generates an image based on a text description and configuration.

#### Parameters

- params: GenerateImagesParametersThe parameters for generating images.

#### Returns Promise&lt;GenerateImagesResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.generateImages({
 model: 'imagen-3.0-generate-002',
 prompt: 'Robot holding a red skateboard',
 config: {
   numberOfImages: 1,
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:375

### generateVideos

- generateVideos ( params : GenerateVideosParameters , ) : Promise &lt; GenerateVideosOperation &gt; Generates videos based on a text description and configuration. Parameters Returns Promise &lt; GenerateVideosOperation &gt; A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method. Example const operation = await ai . models . generateVideos ({ model: 'veo-2.0-generate-001' , prompt: 'A neon hologram of a cat driving at top speed' , config: { numberOfVideos: 1 }); while (! operation . done ) { await new Promise ( resolve =&gt; setTimeout ( resolve , 10000 )); operation = await ai . operations . getVideosOperation ({ operation: operation }); } console . log ( operation . response ?. generatedVideos ?.[ 0 ]?. video ?. uri ); Copy
- Generates videos based on a text description and configuration.

#### Parameters

- params: GenerateVideosParametersThe parameters for generating videos.

#### Returns Promise&lt;GenerateVideosOperation&gt;

A Promise which allows you to track the progress and eventually retrieve the generated videos using the operations.get method.

#### Example

```
const operation = await ai.models.generateVideos({
 model: 'veo-2.0-generate-001',
 prompt: 'A neon hologram of a cat driving at top speed',
 config: {
   numberOfVideos: 1
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({operation: operation});
}

console.log(operation.response?.generatedVideos?.[0]?.video?.uri);
Copy
```

- Defined in models.ts:1502

### get

- get ( params : GetModelParameters ) : Promise &lt; Model &gt; Fetches information about a model by name. Parameters Returns Promise &lt; Model &gt; Example const modelInfo = await ai . models . get ({ model: 'gemini-2.0-flash' }); Copy
- Fetches information about a model by name.

#### Parameters

- params: GetModelParameters

#### Returns Promise&lt;Model&gt;

#### Example

```
const modelInfo = await ai.models.get({model: 'gemini-2.0-flash'});
Copy
```

- Defined in models.ts:993

### list

- list ( params ?: ListModelsParameters ) : Promise &lt; Pager &lt; Model &gt; &gt; Parameters Returns Promise &lt; Pager &lt; Model &gt; &gt;

#### Parameters

- Optionalparams: ListModelsParameters

#### Returns Promise&lt;Pager&lt;Model&gt;&gt;

- Defined in models.ts:411

### update

- update ( params : UpdateModelParameters ) : Promise &lt; Model &gt; Updates a tuned model by its name. Parameters Returns Promise &lt; Model &gt; The response from the API. Example const response = await ai . models . update ({ model: 'tuned-model-name' , config: { displayName: 'New display name' , description: 'New description' , }, }); Copy
- Updates a tuned model by its name.

#### Parameters

- params: UpdateModelParametersThe parameters for updating the model.

#### Returns Promise&lt;Model&gt;

The response from the API.

#### Example

```
const response = await ai.models.update({
  model: 'tuned-model-name',
  config: {
    displayName: 'New display name',
    description: 'New description',
  },
});
Copy
```

- Defined in models.ts:1159

### upscaleImage

- upscaleImage ( params : UpscaleImageParameters ) : Promise &lt; UpscaleImageResponse &gt; Upscales an image based on an image, upscale factor, and configuration.Only supported in Vertex AI currently. Parameters Returns Promise &lt; UpscaleImageResponse &gt; The response from the API. Example const response = await client . models . upscaleImage ({ model: 'imagen-3.0-generate-002' , image: image , upscaleFactor: 'x2' , config: { includeRaiReason: true , }, }); console . log ( response ?. generatedImages ?.[ 0 ]?. image ?. imageBytes ); Copy
- Upscales an image based on an image, upscale factor, and configuration.
Only supported in Vertex AI currently.

#### Parameters

- params: UpscaleImageParametersThe parameters for upscaling an image.

#### Returns Promise&lt;UpscaleImageResponse&gt;

The response from the API.

#### Example

```
const response = await client.models.upscaleImage({
 model: 'imagen-3.0-generate-002',
 image: image,
 upscaleFactor: 'x2',
 config: {
   includeRaiReason: true,
 },
});
console.log(response?.generatedImages?.[0]?.image?.imageBytes);
Copy
```

- Defined in models.ts:504

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Files | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/files.Files.html#get

# Class Files

#### Hierarchy

- BaseModule
    - Files

- Defined in files.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Files ( apiClient : ApiClient ) : Files Parameters Returns Files Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Files

Overrides BaseModule.constructor

- Defined in files.ts:17

Methods

### delete

- delete ( params : DeleteFileParameters ) : Promise &lt; DeleteFileResponse &gt; Deletes a remotely stored file. Parameters Returns Promise &lt; DeleteFileResponse &gt; The DeleteFileResponse, the response for the delete method. Example The following code deletes an example file named "files/mehozpxf877d". await ai . files . delete ({ name: file . name }); Copy
- Deletes a remotely stored file.

#### Parameters

- params: DeleteFileParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteFileResponse&gt;

The DeleteFileResponse, the response for the delete method.

#### Example

The following code deletes an example file named "files/mehozpxf877d".

```
await ai.files.delete({name: file.name});
Copy
```

- Defined in files.ts:288

### download

- download ( params : DownloadFileParameters ) : Promise &lt; void &gt; Downloads a remotely stored file asynchronously to a location specified inthe params object. This method only works on Node environment, todownload files in the browser, use a browser compliant method like an tag. Parameters Returns Promise &lt; void &gt; Example The following code downloads an example file named "files/mehozpxf877d" as"file.txt". await ai . files . download ({ file: file . name , downloadPath: 'file.txt' }); Copy
- Downloads a remotely stored file asynchronously to a location specified in
the params object. This method only works on Node environment, to
download files in the browser, use a browser compliant method like an 
tag.

#### Parameters

- params: DownloadFileParametersThe parameters for the download request.

#### Returns Promise&lt;void&gt;

#### Example

The following code downloads an example file named "files/mehozpxf877d" as
"file.txt".

```
await ai.files.download({file: file.name, downloadPath: 'file.txt'});
Copy
```

- Defined in files.ts:124

### get

- get ( params : GetFileParameters ) : Promise &lt; File &gt; Retrieves the file information from the service. Parameters Returns Promise &lt; File &gt; The Promise that resolves to the types.File object requested. Example const config : GetFileParameters = { name: fileName , }; file = await ai . files . get ( config ); console . log ( file . name ); Copy
- Retrieves the file information from the service.

#### Parameters

- params: GetFileParametersThe parameters for the get request

#### Returns Promise&lt;File&gt;

The Promise that resolves to the types.File object requested.

#### Example

```
const config: GetFileParameters = {
  name: fileName,
};
file = await ai.files.get(config);
console.log(file.name);
Copy
```

- Defined in files.ts:235

### list

- list ( params ?: ListFilesParameters ) : Promise &lt; Pager &lt; File &gt; &gt; Lists all current project files from the service. Parameters Returns Promise &lt; Pager &lt; File &gt; &gt; The paginated results of the list of files Example The following code prints the names of all files from the service, thesize of each page is 10. const listResponse = await ai . files . list ({ config: { 'pageSize' : 10 }}); for await ( const file of listResponse ) { console . log ( file . name ); } Copy
- Lists all current project files from the service.

#### Parameters

- params: ListFilesParameters = {}The parameters for the list request

#### Returns Promise&lt;Pager&lt;File&gt;&gt;

The paginated results of the list of files

#### Example

The following code prints the names of all files from the service, the
size of each page is 10.

```
const listResponse = await ai.files.list({config: {'pageSize': 10}});
for await (const file of listResponse) {
  console.log(file.name);
}
Copy
```

- Defined in files.ts:38

### upload

- upload ( params : UploadFileParameters ) : Promise &lt; File &gt; Uploads a file asynchronously to the Gemini API.This method is not available in Vertex AI.Supported upload sources: Parameters Returns Promise &lt; File &gt; A promise that resolves to a types.File object. Remarks The mimeType can be specified in the config parameter. If omitted: This section can contain multiple paragraphs and code examples. See types.UploadFileParameters#config for the optionalconfig in the parameters. Throws An error if called on a Vertex AI client. Throws An error if the mimeType is not provided and can not be inferred,the mimeType can be provided in the params.config parameter. Throws An error occurs if a suitable upload location cannot be established. Example The following code uploads a file to Gemini API. const file = await ai . files . upload ({ file: 'file.txt' , config: { mimeType: 'text/plain' , }}); console . log ( file . name ); Copy
- Uploads a file asynchronously to the Gemini API.
This method is not available in Vertex AI.
Supported upload sources:
    - Node.js: File path (string) or Blob object.
    - Browser: Blob object (e.g., File).

#### Parameters

- params: UploadFileParametersOptional parameters specified in the
types.UploadFileParameters interface.

#### Returns Promise&lt;File&gt;

A promise that resolves to a types.File object.

#### Remarks

The mimeType can be specified in the config parameter. If omitted:

- For file path (string) inputs, the mimeType will be inferred from the
file extension.
- For Blob object inputs, the mimeType will be set to the Blob's type
property.
Somex eamples for file extension to mimeType mapping:
.txt -&gt; text/plain
.json -&gt; application/json
.jpg  -&gt; image/jpeg
.png -&gt; image/png
.mp3 -&gt; audio/mpeg
.mp4 -&gt; video/mp4

This section can contain multiple paragraphs and code examples.

#### See

types.UploadFileParameters#config for the optional
config in the parameters.

#### Throws

An error if called on a Vertex AI client.

#### Throws

An error if the mimeType is not provided and can not be inferred,
the mimeType can be provided in the params.config parameter.

#### Throws

An error occurs if a suitable upload location cannot be established.

#### Example

The following code uploads a file to Gemini API.

```
const file = await ai.files.upload({file: 'file.txt', config: {
  mimeType: 'text/plain',
}});
console.log(file.name);
Copy
```

- Defined in files.ts:92

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## Live | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/live.Live.html#connect

# Class LiveExperimental

Live class encapsulates the configuration for live interaction with the
Generative Language API. It embeds ApiClient for general API settings.

- Defined in live.ts:71

Index

### Constructors

### Properties

### Methods

Constructors

### constructor

- new Live ( apiClient : ApiClient , auth : Auth , webSocketFactory : WebSocketFactory , ) : Live Experimental Parameters Returns Live
- ```
Experimental
```

#### Parameters

- apiClient: ApiClient
- auth: Auth
- webSocketFactory: WebSocketFactory

#### Returns Live

- Defined in live.ts:74

Properties

### Readonly Experimentalmusic

- Defined in live.ts:72

Methods

### connect

- connect ( params : LiveConnectParameters ) : Promise &lt; Session &gt; Experimental Establishes a connection to the specified model with the givenconfiguration and returns a Session object representing that connection. Built-in MCP support is an experimental feature, may change infuture versions. Parameters Returns Promise &lt; Session &gt; A live session. Remarks Example let model : string ; if ( GOOGLE\_GENAI\_USE\_VERTEXAI ) { model = 'gemini-2.0-flash-live-preview-04-09' ; } else { model = 'gemini-2.0-flash-live-001' ; } const session = await ai . live . connect ({ model: model , config: { responseModalities: [ Modality . AUDIO ], }, callbacks: { onopen : () =&gt; { console . log ( 'Connected to the socket.' ); }, onmessage : ( e : MessageEvent ) =&gt; { console . log ( 'Received message from the server: %s \n ' , debug ( e . data )); }, onerror : ( e : ErrorEvent ) =&gt; { console . log ( 'Error occurred: %s \n ' , debug ( e . error )); }, onclose : ( e : CloseEvent ) =&gt; { console . log ( 'Connection closed.' ); }, }, }); Copy
- ```
Experimental
```
- Establishes a connection to the specified model with the given
configuration and returns a Session object representing that connection.
- Built-in MCP support is an experimental feature, may change in
future versions.

#### Parameters

- params: LiveConnectParametersThe parameters for establishing a connection to the model.

#### Returns Promise&lt;Session&gt;

A live session.

#### Remarks

#### Example

```
let model: string;
if (GOOGLE_GENAI_USE_VERTEXAI) {
  model = 'gemini-2.0-flash-live-preview-04-09';
} else {
  model = 'gemini-2.0-flash-live-001';
}
const session = await ai.live.connect({
  model: model,
  config: {
    responseModalities: [Modality.AUDIO],
  },
  callbacks: {
    onopen: () => {
      console.log('Connected to the socket.');
    },
    onmessage: (e: MessageEvent) => {
      console.log('Received message from the server: %s\n', debug(e.data));
    },
    onerror: (e: ErrorEvent) => {
      console.log('Error occurred: %s\n', debug(e.error));
    },
    onclose: (e: CloseEvent) => {
      console.log('Connection closed.');
    },
  },
});
Copy
```

- Defined in live.ts:128

Settings

On This Page

Constructors

Properties

Methods

- Loading...

Generated using TypeDoc

---

## tunings | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/tunings.html

# Module tunings

Classes

Settings

On This Page

Classes

- Loading...

Generated using TypeDoc

---

## Caches | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/caches.Caches.html#create

# Class Caches

#### Hierarchy

- BaseModule
    - Caches

- Defined in caches.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Caches ( apiClient : ApiClient ) : Caches Parameters Returns Caches Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Caches

Overrides BaseModule.constructor

- Defined in caches.ts:17

Methods

### create

- create ( params : CreateCachedContentParameters ) : Promise &lt; CachedContent &gt; Creates a cached contents resource. Parameters Returns Promise &lt; CachedContent &gt; The created cached content. Remarks Context caching is only supported for specific models. See GeminiDeveloper API reference and Vertex AI reference for more information. Example const contents = ...; // Initialize the content to cache. const response = await ai . caches . create ({ model: 'gemini-2.0-flash-001' , config: { 'contents' : contents , 'displayName' : 'test cache' , 'systemInstruction' : 'What is the sum of the two pdfs?' , 'ttl' : '86400s' , } }); Copy
- Creates a cached contents resource.

#### Parameters

- params: CreateCachedContentParametersThe parameters for the create request.

#### Returns Promise&lt;CachedContent&gt;

The created cached content.

#### Remarks

Context caching is only supported for specific models. See Gemini
Developer API reference
and Vertex AI reference
for more information.

#### Example

```
const contents = ...; // Initialize the content to cache.
const response = await ai.caches.create({
  model: 'gemini-2.0-flash-001',
  config: {
   'contents': contents,
   'displayName': 'test cache',
   'systemInstruction': 'What is the sum of the two pdfs?',
   'ttl': '86400s',
 }
});
Copy
```

- Defined in caches.ts:72

### delete

- delete ( params : DeleteCachedContentParameters , ) : Promise &lt; DeleteCachedContentResponse &gt; Deletes cached content. Parameters Returns Promise &lt; DeleteCachedContentResponse &gt; The empty response returned by the API. Example await ai . caches . delete ({ name: '...' }); // The server-generated resource name. Copy
- Deletes cached content.

#### Parameters

- params: DeleteCachedContentParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteCachedContentResponse&gt;

The empty response returned by the API.

#### Example

```
await ai.caches.delete({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:252

### get

- get ( params : GetCachedContentParameters ) : Promise &lt; CachedContent &gt; Gets cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The cached content. Example await ai . caches . get ({ name: '...' }); // The server-generated resource name. Copy
- Gets cached content configurations.

#### Parameters

- params: GetCachedContentParametersThe parameters for the get request.

#### Returns Promise&lt;CachedContent&gt;

The cached content.

#### Example

```
await ai.caches.get({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:162

### list

- list ( params ?: ListCachedContentsParameters ) : Promise &lt; Pager &lt; CachedContent &gt; &gt; Lists cached content configurations. Parameters Returns Promise &lt; Pager &lt; CachedContent &gt; &gt; The paginated results of the list of cached contents. Example const cachedContents = await ai . caches . list ({ config: { 'pageSize' : 2 }}); for ( const cachedContent of cachedContents ) { console . log ( cachedContent ); } Copy
- Lists cached content configurations.

#### Parameters

- params: ListCachedContentsParameters = {}The parameters for the list request.

#### Returns Promise&lt;Pager&lt;CachedContent&gt;&gt;

The paginated results of the list of cached contents.

#### Example

```
const cachedContents = await ai.caches.list({config: {'pageSize': 2}});
for (const cachedContent of cachedContents) {
  console.log(cachedContent);
}
Copy
```

- Defined in caches.ts:35

### update

- update ( params : UpdateCachedContentParameters ) : Promise &lt; CachedContent &gt; Updates cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The updated cached content. Example const response = await ai . caches . update ({ name: '...' , // The server-generated resource name. config: { 'ttl' : '7600s' } }); Copy
- Updates cached content configurations.

#### Parameters

- params: UpdateCachedContentParametersThe parameters for the update request.

#### Returns Promise&lt;CachedContent&gt;

The updated cached content.

#### Example

```
const response = await ai.caches.update({
  name: '...',  // The server-generated resource name.
  config: {'ttl': '7600s'}
});
Copy
```

- Defined in caches.ts:341

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## music | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/modules/music.html

# Module music

Classes

Settings

On This Page

Classes

- Loading...

Generated using TypeDoc

---

## Caches | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/caches.Caches.html#constructor

# Class Caches

#### Hierarchy

- BaseModule
    - Caches

- Defined in caches.ts:16

Index

### Constructors

### Methods

Constructors

### constructor

- new Caches ( apiClient : ApiClient ) : Caches Parameters Returns Caches Overrides BaseModule.constructor

#### Parameters

- apiClient: ApiClient

#### Returns Caches

Overrides BaseModule.constructor

- Defined in caches.ts:17

Methods

### create

- create ( params : CreateCachedContentParameters ) : Promise &lt; CachedContent &gt; Creates a cached contents resource. Parameters Returns Promise &lt; CachedContent &gt; The created cached content. Remarks Context caching is only supported for specific models. See GeminiDeveloper API reference and Vertex AI reference for more information. Example const contents = ...; // Initialize the content to cache. const response = await ai . caches . create ({ model: 'gemini-2.0-flash-001' , config: { 'contents' : contents , 'displayName' : 'test cache' , 'systemInstruction' : 'What is the sum of the two pdfs?' , 'ttl' : '86400s' , } }); Copy
- Creates a cached contents resource.

#### Parameters

- params: CreateCachedContentParametersThe parameters for the create request.

#### Returns Promise&lt;CachedContent&gt;

The created cached content.

#### Remarks

Context caching is only supported for specific models. See Gemini
Developer API reference
and Vertex AI reference
for more information.

#### Example

```
const contents = ...; // Initialize the content to cache.
const response = await ai.caches.create({
  model: 'gemini-2.0-flash-001',
  config: {
   'contents': contents,
   'displayName': 'test cache',
   'systemInstruction': 'What is the sum of the two pdfs?',
   'ttl': '86400s',
 }
});
Copy
```

- Defined in caches.ts:72

### delete

- delete ( params : DeleteCachedContentParameters , ) : Promise &lt; DeleteCachedContentResponse &gt; Deletes cached content. Parameters Returns Promise &lt; DeleteCachedContentResponse &gt; The empty response returned by the API. Example await ai . caches . delete ({ name: '...' }); // The server-generated resource name. Copy
- Deletes cached content.

#### Parameters

- params: DeleteCachedContentParametersThe parameters for the delete request.

#### Returns Promise&lt;DeleteCachedContentResponse&gt;

The empty response returned by the API.

#### Example

```
await ai.caches.delete({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:252

### get

- get ( params : GetCachedContentParameters ) : Promise &lt; CachedContent &gt; Gets cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The cached content. Example await ai . caches . get ({ name: '...' }); // The server-generated resource name. Copy
- Gets cached content configurations.

#### Parameters

- params: GetCachedContentParametersThe parameters for the get request.

#### Returns Promise&lt;CachedContent&gt;

The cached content.

#### Example

```
await ai.caches.get({name: '...'}); // The server-generated resource name.
Copy
```

- Defined in caches.ts:162

### list

- list ( params ?: ListCachedContentsParameters ) : Promise &lt; Pager &lt; CachedContent &gt; &gt; Lists cached content configurations. Parameters Returns Promise &lt; Pager &lt; CachedContent &gt; &gt; The paginated results of the list of cached contents. Example const cachedContents = await ai . caches . list ({ config: { 'pageSize' : 2 }}); for ( const cachedContent of cachedContents ) { console . log ( cachedContent ); } Copy
- Lists cached content configurations.

#### Parameters

- params: ListCachedContentsParameters = {}The parameters for the list request.

#### Returns Promise&lt;Pager&lt;CachedContent&gt;&gt;

The paginated results of the list of cached contents.

#### Example

```
const cachedContents = await ai.caches.list({config: {'pageSize': 2}});
for (const cachedContent of cachedContents) {
  console.log(cachedContent);
}
Copy
```

- Defined in caches.ts:35

### update

- update ( params : UpdateCachedContentParameters ) : Promise &lt; CachedContent &gt; Updates cached content configurations. Parameters Returns Promise &lt; CachedContent &gt; The updated cached content. Example const response = await ai . caches . update ({ name: '...' , // The server-generated resource name. config: { 'ttl' : '7600s' } }); Copy
- Updates cached content configurations.

#### Parameters

- params: UpdateCachedContentParametersThe parameters for the update request.

#### Returns Promise&lt;CachedContent&gt;

The updated cached content.

#### Example

```
const response = await ai.caches.update({
  name: '...',  // The server-generated resource name.
  config: {'ttl': '7600s'}
});
Copy
```

- Defined in caches.ts:341

Settings

On This Page

Constructors

Methods

- Loading...

Generated using TypeDoc

---

## EmbedContentResponse | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/classes/types.EmbedContentResponse.html

# Class EmbedContentResponse

Response for the embed\_content method.

- Defined in types.ts:2318

Index

### Constructors

### Properties

Constructors

### constructor

- new EmbedContentResponse(): EmbedContentResponseReturns EmbedContentResponse

Properties

### Optionalembeddings

The embeddings for each request, in the same order as provided in
the batch request.

- Defined in types.ts:2322

### Optionalmetadata

Vertex API only. Metadata about the request.

- Defined in types.ts:2325

Settings

On This Page

Constructors

Properties

- Loading...

Generated using TypeDoc

---

## File | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.File.html

# Interface File

A file uploaded to the API.

- Defined in types.ts:3564

Index

### Properties

Properties

### OptionalcreateTime

Output only. The timestamp of when the File was created.

- Defined in types.ts:3574

### OptionaldisplayName

Optional. The human-readable display name for the File. The display name must be no more than 512 characters in length, including spaces. Example: 'Welcome Image'

- Defined in types.ts:3568

### OptionaldownloadUri

Output only. The URI of the File, only set for downloadable (generated) files.

- Defined in types.ts:3584

### Optionalerror

Output only. Error status if File processing failed.

- Defined in types.ts:3592

### OptionalexpirationTime

Output only. The timestamp of when the File will be deleted. Only set if the File is scheduled to expire.

- Defined in types.ts:3576

### OptionalmimeType

Output only. MIME type of the file.

- Defined in types.ts:3570

### Optionalname

The File resource name. The ID (name excluding the "files/" prefix) can contain up to 40 characters that are lowercase alphanumeric or dashes (-). The ID cannot start or end with a dash. If the name is empty on create, a unique name will be generated. Example: files/123-456

- Defined in types.ts:3566

### Optionalsha256Hash

Output only. SHA-256 hash of the uploaded bytes. The hash value is encoded in base64 format.

- Defined in types.ts:3580

### OptionalsizeBytes

Output only. Size of the file in bytes.

- Defined in types.ts:3572

### Optionalsource

Output only. The source of the File.

- Defined in types.ts:3588

### Optionalstate

Output only. Processing state of the File.

- Defined in types.ts:3586

### OptionalupdateTime

Output only. The timestamp of when the File was last updated.

- Defined in types.ts:3578

### Optionaluri

Output only. The URI of the File.

- Defined in types.ts:3582

### OptionalvideoMetadata

Output only. Metadata for a video.

- Defined in types.ts:3590

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

## UploadFileParameters | @google/genai

**Source URL:** https://googleapis.github.io/js-genai/release_docs/interfaces/types.UploadFileParameters.html

# Interface UploadFileParameters

Parameters for the upload file method.

- Defined in types.ts:4808

Index

### Properties

Properties

### Optionalconfig

Configuration that contains optional parameters.

- Defined in types.ts:4812

### file

The string path to the file to be uploaded or a Blob object.

- Defined in types.ts:4810

Settings

On This Page

Properties

- Loading...

Generated using TypeDoc

---

