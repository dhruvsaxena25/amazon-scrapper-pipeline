from scrapper.pipeline.url_pipeline import AmazonUrlScrapingPipeline
from scrapper.pipeline.prodcut_pipeline import AmazonProductScrapingPipeline

# Initialize and run
# pipeline = AmazonUrlScrapingPipeline(
#     search_terms=['laptop pc', 'wireless mouse'],
#     target_links=1,  # 1 link for each search term
#     headless=False
# )

# url_artifact = pipeline.run()
# print(f"URLs saved to: {url_artifact.url_file_path}")


# # Initialize with URL file path
# pipeline = AmazonProductScrapingPipeline(
#     url_file_path="./example_url.json",
#     headless=False
# )
# product_artifact = pipeline.run()
# print(f"Products saved to: {product_artifact.product_file_path}")
# print(f"Success: {product_artifact.scraped_count}")



