import typer
app=typer.Typer()
@app.command()
def simulate_network(failures:int=2):print({"simulated_failures":failures,"retry":"exponential backoff expected by adapter"})
if __name__=="__main__":app()
