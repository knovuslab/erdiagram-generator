# ER Diagram Generator

Hello Developers! We're excited to share a tool that has become an essential part of our daily workflow when designing ER diagrams for projects. The `erdiagram-generator` allows you to generate a format called Mermaid, which can be easily imported into draw.io.


## Repository
[erdiagram-generator on GitHub](https://github.com/knovuslab/erdiagram-generator)

## Features
- Open Source: We welcome contributors to join us in enhancing this tool.
- Written in Python: Making it easy to contribute and expand.
- Supports MySQL: Currently, only MySQL DB is supported, but we're looking forward to the open-source community helping us add more drivers for MongoDB, PostgreSQL, DynamoDB, and other databases.

## Getting Started

1. **Clone the Repository**

    ```sh
    git clone https://github.com/knovuslab/erdiagram-generator
    cd erdiagram-generator
    ```

2. **Set Up Virtual Environment**

    ```sh
    mkdir generate
    python -m venv venv
    source ./venv/bin/activate  # Use `venv\Scripts\activate` for Windows
    ```

    Make sure to create the `generated` folder if it doesn't exist:

    ```sh
    mkdir generated
    ```

3. **Configure Database Connection**

    Edit the `.env` file with your database connection details.

4. **Generate ER Diagram**

    ```sh
    python generate
    ```

    This command will generate a `.mmd` file inside the `generated` folder.

5. **Import to draw.io**

    - Open [draw.io](https://www.draw.io).
    - Go to `Arrange -> Insert -> Advanced -> Mermaid`.
    - Import the generated `.mmd` file.

![ER Diagram Generator Example](https://github.com/knovuslab/erdiagram-generator/raw/main/how.PNG)


  

## Contributing

We encourage you to contribute to `erdiagram-generator`! We are looking forward to incorporating more database drivers and enhancing the functionality of the tool. Please read our [contributing guidelines](CONTRIBUTING.md) for details on the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [Mermaid](https://mermaid-js.github.io/mermaid/#/) for providing a markdown-like syntax for generating diagrams.
- [draw.io](https://www.draw.io) for being a versatile diagramming tool.

