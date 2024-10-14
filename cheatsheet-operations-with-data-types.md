**Cheatsheet: Operations with Data Types**

In this section, you learned that:

*   Lists, strings, and tuples have a **positive index** system:
    

```python 
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
0      1      2      3      4      5      6
```

*   And they have a **negative index** system as well:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]  -7     -6     -5     -4     -3     -2     -1   `

*   In a list, the **2nd**, **3rd**, and **4th** items can be accessed with:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]days[1:4]Output: ['Tue', 'Wed', 'Thu']   `

*   **First three items of a list**:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]days[:3]Output:['Mon', 'Tue', 'Wed']` 

*   **Last three items of a list**:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]days[-3:]Output: ['Fri', 'Sat', 'Sun']   `

*   **Everything but the last**:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]days[:-1] Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']` 

*   **Everything but the last two**:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]days[:-2] Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']` 

*   A dictionary **value** can be accessed using its corresponding dictionary **key**:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   phone_numbers = {"John":"+37682929928","Marry":"+423998200919"}phone_numbers["Marry"]Output: '+423998200919'   `
