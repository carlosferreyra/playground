// Generic type for API responses
type ApiResponse<T> = {
	data: T;
	status: number;
	message: string;
};

// Example interface using utility types
interface BaseUser {
	id: number;
	name: string;
	email: string;
}

type UserCreateInput = Omit<BaseUser, 'id'>;
type UserUpdateInput = Partial<BaseUser>;

// Example class with generics and async methods
class DataService<T extends BaseUser> {
	private items: T[] = [];

	async create(input: UserCreateInput): Promise<ApiResponse<T>> {
		try {
			const newItem = {
				...input,
				id: Date.now(),
			} as T;

			this.items.push(newItem);

			return {
				data: newItem,
				status: 201,
				message: 'Created successfully',
			};
		} catch (error) {
			throw new Error(
				`Failed to create: ${error instanceof Error ? error.message : 'Unknown error'}`
			);
		}
	}

	async findById(id: number): Promise<T | undefined> {
		return this.items.find((item) => item.id === id);
	}
}

// Example of a custom type guard
function isValidUser(user: unknown): user is BaseUser {
	return (
		typeof user === 'object' && user !== null && 'id' in user && 'name' in user && 'email' in user
	);
}

// Usage example with async/await and error handling
async function example() {
	const userService = new DataService<BaseUser>();

	try {
		const response = await userService.create({
			name: 'John Doe',
			email: 'john@example.com',
		});

		console.log(response.data);
	} catch (error) {
		console.error('Error:', error instanceof Error ? error.message : 'Unknown error');
	}
}
