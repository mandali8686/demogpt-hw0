# Vandy Info: A Streamlit App for Summarizing Vanderbilt University Information

## Description

This Streamlit application, Vandy Info, is designed to provide a summarized overview of information related to Vanderbilt University. The user inputs a website link containing the relevant information, and the app generates a concise summary using language models.

## Requirements

- Python 3.x
- Streamlit
- langchain
- tempfile

To install the requirements, you can use:

```bash
pip install streamlit langchain
```

## How it Works

1. **Input**: The user enters a website link containing information about Vanderbilt University.

2. **Web Scraping**: The content of the website is fetched and loaded as a Document object.

3. **Text Summarization**: The content is summarized using a language model from the `langchain` library.

4. **Output**: The summarized information is displayed to the user.

## Code Structure

- `st.title("Vandy Info")`: Sets the title of the Streamlit app.
  
### State Variables

- `website_link`: Stores the website link entered by the user.
- `website_content_string`: Holds the content of the website.
- `summary`: Stores the generated summary of the website content.

### Functions

- `load_website_content(website_link)`: Loads the website content from the given link.
  
- `universitySummaryGenerator(website_content_string)`: Generates a summary of the website content using a language model.

### Streamlit UI

- `st.text_input("Enter the website link")`: Text input for the user to enter the website link.
  
- `st.button("Submit")`: Button for submitting the entered website link.

- `st.markdown(summary)`: Displays the generated summary to the user.

## Usage

1. Run the Streamlit app using the following command:

```bash
streamlit run <path-to-the-script>
```

2. Input the website link in the text box and click "Submit".

3. The generated summary will be displayed below the "Submit" button.

## Note

- The language model used is specified as "gpt-3.5-turbo-16k", and its temperature is set to 0 for deterministic output.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
