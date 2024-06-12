# Prompts

Types:

```python
from prompt-foundry-sdk.types import PromptConfiguration, PromptDeleteResponse
```

Methods:

- <code title="post /sdk/v1/prompts">client.prompts.<a href="./src/prompt-foundry-sdk/resources/prompts.py">create</a>(\*\*<a href="src/prompt-foundry-sdk/types/prompt_create_params.py">params</a>) -> <a href="./src/prompt-foundry-sdk/types/prompt_configuration.py">PromptConfiguration</a></code>
- <code title="delete /sdk/v1/prompts/{id}">client.prompts.<a href="./src/prompt-foundry-sdk/resources/prompts.py">delete</a>(id) -> <a href="./src/prompt-foundry-sdk/types/prompt_delete_response.py">PromptDeleteResponse</a></code>

# Tools

Types:

```python
from prompt-foundry-sdk.types import Tool, ToolListResponse, ToolDeleteResponse
```

Methods:

- <code title="post /sdk/v1/tools">client.tools.<a href="./src/prompt-foundry-sdk/resources/tools.py">create</a>(\*\*<a href="src/prompt-foundry-sdk/types/tool_create_params.py">params</a>) -> <a href="./src/prompt-foundry-sdk/types/tool.py">Tool</a></code>
- <code title="get /sdk/v1/tools/{id}">client.tools.<a href="./src/prompt-foundry-sdk/resources/tools.py">retrieve</a>(id) -> <a href="./src/prompt-foundry-sdk/types/tool.py">Tool</a></code>
- <code title="put /sdk/v1/tools/{id}">client.tools.<a href="./src/prompt-foundry-sdk/resources/tools.py">update</a>(id, \*\*<a href="src/prompt-foundry-sdk/types/tool_update_params.py">params</a>) -> <a href="./src/prompt-foundry-sdk/types/tool.py">Tool</a></code>
- <code title="get /sdk/v1/tools">client.tools.<a href="./src/prompt-foundry-sdk/resources/tools.py">list</a>() -> <a href="./src/prompt-foundry-sdk/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="delete /sdk/v1/tools/{id}">client.tools.<a href="./src/prompt-foundry-sdk/resources/tools.py">delete</a>(id) -> <a href="./src/prompt-foundry-sdk/types/tool_delete_response.py">ToolDeleteResponse</a></code>

# EvaluationAssertions

Types:

```python
from prompt-foundry-sdk.types import EvaluationAssertion, EvaluationAssertionListResponse, EvaluationAssertionDeleteResponse
```

Methods:

- <code title="post /sdk/v1/evaluation-assertions">client.evaluation_assertions.<a href="./src/prompt-foundry-sdk/resources/evaluation_assertions.py">create</a>(\*\*<a href="src/prompt-foundry-sdk/types/evaluation_assertion_create_params.py">params</a>) -> <a href="./src/prompt-foundry-sdk/types/evaluation_assertion.py">EvaluationAssertion</a></code>
- <code title="get /sdk/v1/evaluation-assertions/{id}">client.evaluation_assertions.<a href="./src/prompt-foundry-sdk/resources/evaluation_assertions.py">retrieve</a>(id) -> <a href="./src/prompt-foundry-sdk/types/evaluation_assertion.py">EvaluationAssertion</a></code>
- <code title="put /sdk/v1/evaluation-assertions/{id}">client.evaluation_assertions.<a href="./src/prompt-foundry-sdk/resources/evaluation_assertions.py">update</a>(id, \*\*<a href="src/prompt-foundry-sdk/types/evaluation_assertion_update_params.py">params</a>) -> <a href="./src/prompt-foundry-sdk/types/evaluation_assertion.py">EvaluationAssertion</a></code>
- <code title="get /sdk/v1/evaluation-assertions">client.evaluation_assertions.<a href="./src/prompt-foundry-sdk/resources/evaluation_assertions.py">list</a>(\*\*<a href="src/prompt-foundry-sdk/types/evaluation_assertion_list_params.py">params</a>) -> <a href="./src/prompt-foundry-sdk/types/evaluation_assertion_list_response.py">EvaluationAssertionListResponse</a></code>
- <code title="delete /sdk/v1/evaluation-assertions/{id}">client.evaluation_assertions.<a href="./src/prompt-foundry-sdk/resources/evaluation_assertions.py">delete</a>(id) -> <a href="./src/prompt-foundry-sdk/types/evaluation_assertion_delete_response.py">EvaluationAssertionDeleteResponse</a></code>

# Evaluations

Types:

```python
from prompt-foundry-sdk.types import Evaluation, EvaluationListResponse, EvaluationDeleteResponse
```

Methods:

- <code title="post /sdk/v1/evaluations">client.evaluations.<a href="./src/prompt-foundry-sdk/resources/evaluations.py">create</a>(\*\*<a href="src/prompt-foundry-sdk/types/evaluation_create_params.py">params</a>) -> <a href="./src/prompt-foundry-sdk/types/evaluation.py">Evaluation</a></code>
- <code title="get /sdk/v1/evaluations/{id}">client.evaluations.<a href="./src/prompt-foundry-sdk/resources/evaluations.py">retrieve</a>(id) -> <a href="./src/prompt-foundry-sdk/types/evaluation.py">Evaluation</a></code>
- <code title="put /sdk/v1/evaluations/{id}">client.evaluations.<a href="./src/prompt-foundry-sdk/resources/evaluations.py">update</a>(id, \*\*<a href="src/prompt-foundry-sdk/types/evaluation_update_params.py">params</a>) -> <a href="./src/prompt-foundry-sdk/types/evaluation.py">Evaluation</a></code>
- <code title="get /sdk/v1/evaluations">client.evaluations.<a href="./src/prompt-foundry-sdk/resources/evaluations.py">list</a>() -> <a href="./src/prompt-foundry-sdk/types/evaluation_list_response.py">EvaluationListResponse</a></code>
- <code title="delete /sdk/v1/evaluations/{id}">client.evaluations.<a href="./src/prompt-foundry-sdk/resources/evaluations.py">delete</a>(id) -> <a href="./src/prompt-foundry-sdk/types/evaluation_delete_response.py">EvaluationDeleteResponse</a></code>
