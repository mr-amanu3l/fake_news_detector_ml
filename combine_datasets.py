import pandas as pd

def combine_fake_real():
    fake_df = pd.read_csv('Fake.csv')
    real_df = pd.read_csv('True.csv')

    fake_df['label'] = 'fake'
    real_df['label'] = 'real'

    fake_df = fake_df[['title', 'text', 'label']]
    real_df = real_df[['title', 'text', 'label']]

    combined_df = pd.concat([fake_df, real_df], ignore_index=True)
    combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

    combined_df.to_csv('fake_news.csv', index=False)
    print("Combined dataset saved as 'fake_news.csv'.")

if __name__ == "__main__":
    combine_fake_real()
