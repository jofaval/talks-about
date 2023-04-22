using System;
using System.Collections.Generic;

public class Product {
    public string description;
    public int id;
    public string imageUrl;
    public string name;
    public float price;
    public string url;
}

public interface ScraperEntity<Type>
{
    Type scrape();
}

public class Scraper
{
    private bool isInvalidUrl(string url)
    {
        return false;
    }

    private string getContentFromUrl(string url)
    {
        throw new NotImplementedException("Scraper::getContentFromUrl is not yet implemented");
    }

    public string scrapeUrl(string url)
    {
        if (this.isInvalidUrl(url))
        {
            throw new Exception("The given URL is invalid");
        }

        return this.getContentFromUrl(url);
    }

    // TODO: implement pagination
}

public class ProductScraper : Scraper, ScraperEntity<Product>
{
    private string url;

    public ProductScraper(string url)
    {
        this.url = url;
    }

    public Product scrape()
    {
        var content = this.scrapeUrl(this.url);

        throw new NotImplementedException("ProductScraper::scrape is not yet implemented");
    }
}

public class CatalogScraper : Scraper, ScraperEntity<HashSet<string>>
{
    private string url;

    public CatalogScraper(string url)
    {
        this.url = url;
    }

    public HashSet<string> scrape()
    {
        var content = this.scrapeUrl(this.url);

        throw new NotImplementedException("CatalogScraper::scrape is not yet implemented");
    }
}

public class WebScrapingOrchestrator
{
    private string baseUrl;

    public WebScrapingOrchestrator(string baseUrl)
    {
        this.baseUrl = baseUrl;
    }

    public List<Product> scrapeProducts(HashSet<string> productsUrls)
    {
        List<Product> productsDetails = new List<Product>();

        // TODO: implement multithreading
        foreach (var productUrl in productsUrls)
        {
            var productScraper = new ProductScraper(productUrl);
            productsDetails.Add(productScraper.scrape());
        }

        return productsDetails;
    }

    public List<Product> start()
    {
        var catalog = new CatalogScraper(this.baseUrl);
        var productsUrls = catalog.scrape();
        var productsDetails = this.scrapeProducts(productsUrls);

        return productsDetails;
    }
}

public class CSharpWebScraperExample
{
    private bool saveToCsv(List<Product> products)
    {
        throw new NotImplementedException("CSharpWebScraperExample::saveToCsv is not yet implemented");
    }

    private void printResult(bool success)
    {
        if (success)
        {
            System.Console.WriteLine("Products scraped successfully!");
            return;
        }

        System.Console.WriteLine("Could not scrape products... sorry!!");
    }

    public void start(string url)
    {
        var orchestrator = new WebScrapingOrchestrator(url);
        var products = orchestrator.start();

        var success = this.saveToCsv(products);
        this.printResult(success);
    }

    public static void Main()
    {
        string url = "http://127.0.0.1:5500/web-scraping/sites/awesome-site/e-commerce";
        var instance = new CSharpWebScraperExample();
        instance.start(url);
    }
}