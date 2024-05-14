# Video Search Project

The Video Search project is designed to facilitate searching and retrieving specific segments from a collection of videos. This tool leverages machine learning and natural language processing to understand search queries and return relevant video clips.

## Instructions for Use

1. Clone this repository to your local machine using `git clone` or download the files directly:

    ```sh
    git clone https://github.com/yourusername/video_search.git
    cd video_search
    ```

2. Install the required dependencies by running:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of the project and add your OpenAI API key:

    ```makefile
    OPENAI_API_KEY=your_openai_api_key
    ```

4. Run the Streamlit application by executing the following command:

    ```sh
    streamlit run program.py
    ```

## Project Structure

- **program.py:** The main script to run the Streamlit application.
- **video_lib.py:** Contains functions for processing and searching through videos.
- **requirements.txt:** Lists the required Python libraries.
- **README.md:** Provides an overview and instructions for the project.

## Usage

1. Launch the Streamlit application.
2. Enter your search query in the provided input box.
3. The application will process the query and return relevant video clips.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
